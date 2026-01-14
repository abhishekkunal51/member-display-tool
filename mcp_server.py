"""
MCP Server for Member Display Tool

Provides tools to query and interact with member data from CSV files.
"""

import csv
import os
from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("member-display-tool")

# Default CSV file path
DEFAULT_CSV = "members.csv"


def load_members(filename: str = DEFAULT_CSV) -> list[dict]:
    """Load members from CSV file."""
    if not os.path.exists(filename):
        return []

    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)


@mcp.tool()
def list_members(limit: int = 10, offset: int = 0) -> str:
    """
    List members from the CSV file.

    Args:
        limit: Maximum number of members to return (default 10)
        offset: Number of members to skip (default 0)

    Returns:
        Formatted list of members with their details
    """
    members = load_members()

    if not members:
        return "No members found or file not accessible."

    subset = members[offset:offset + limit]

    if not subset:
        return f"No members found at offset {offset}."

    result = f"Showing members {offset + 1} to {offset + len(subset)} of {len(members)}:\n\n"

    for member in subset:
        result += f"- {member.get('first_name', '')} {member.get('last_name', '')}"
        if member.get('email'):
            result += f" ({member['email']})"
        result += "\n"

    return result


@mcp.tool()
def search_members(query: str) -> str:
    """
    Search members by name or email.

    Args:
        query: Search term to match against first name, last name, or email

    Returns:
        List of matching members
    """
    members = load_members()
    query_lower = query.lower()

    matches = []
    for member in members:
        first_name = member.get('first_name', '').lower()
        last_name = member.get('last_name', '').lower()
        email = member.get('email', '').lower()

        if query_lower in first_name or query_lower in last_name or query_lower in email:
            matches.append(member)

    if not matches:
        return f"No members found matching '{query}'."

    result = f"Found {len(matches)} member(s) matching '{query}':\n\n"

    for member in matches[:20]:  # Limit to 20 results
        result += f"- ID: {member.get('id', 'N/A')}\n"
        result += f"  Name: {member.get('first_name', '')} {member.get('last_name', '')}\n"
        result += f"  Email: {member.get('email', 'N/A')}\n"
        result += f"  Gender: {member.get('gender', 'N/A')}\n\n"

    if len(matches) > 20:
        result += f"... and {len(matches) - 20} more results."

    return result


@mcp.tool()
def get_member_by_id(member_id: int) -> str:
    """
    Get a specific member by their ID.

    Args:
        member_id: The ID of the member to retrieve

    Returns:
        Member details or error message
    """
    members = load_members()

    for member in members:
        if member.get('id') == str(member_id):
            return f"""Member Details:
- ID: {member.get('id')}
- Name: {member.get('first_name', '')} {member.get('last_name', '')}
- Email: {member.get('email', 'N/A')}
- Gender: {member.get('gender', 'N/A')}
- IP Address: {member.get('ip_address', 'N/A')}"""

    return f"No member found with ID {member_id}."


@mcp.tool()
def get_member_count() -> str:
    """
    Get the total number of members in the CSV file.

    Returns:
        Total member count
    """
    members = load_members()
    return f"Total members: {len(members)}"


@mcp.tool()
def get_members_by_gender(gender: str) -> str:
    """
    Filter members by gender.

    Args:
        gender: Gender to filter by (e.g., 'Male', 'Female', 'Non-binary')

    Returns:
        List of members matching the gender filter
    """
    members = load_members()
    gender_lower = gender.lower()

    matches = [m for m in members if m.get('gender', '').lower() == gender_lower]

    if not matches:
        return f"No members found with gender '{gender}'."

    result = f"Found {len(matches)} {gender} member(s):\n\n"

    for member in matches[:20]:
        result += f"- {member.get('first_name', '')} {member.get('last_name', '')} ({member.get('email', 'N/A')})\n"

    if len(matches) > 20:
        result += f"\n... and {len(matches) - 20} more."

    return result


@mcp.tool()
def get_gender_statistics() -> str:
    """
    Get statistics about member genders.

    Returns:
        Gender distribution statistics
    """
    members = load_members()

    if not members:
        return "No members found."

    gender_counts = {}
    for member in members:
        gender = member.get('gender', 'Unknown')
        gender_counts[gender] = gender_counts.get(gender, 0) + 1

    result = f"Gender Statistics (Total: {len(members)} members):\n\n"

    for gender, count in sorted(gender_counts.items(), key=lambda x: -x[1]):
        percentage = (count / len(members)) * 100
        result += f"- {gender}: {count} ({percentage:.1f}%)\n"

    return result


if __name__ == "__main__":
    mcp.run()
