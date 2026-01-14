# Member Display Tool

A Python command-line tool for reading and displaying member names from CSV files. Includes an MCP server for AI integration.

## Features

- Read member data from CSV files
- Display formatted full names (first + last name)
- Comprehensive error handling
- Command-line argument support
- Shows total member count
- **MCP Server** for Claude AI integration

## Installation

1. Clone the repository:
```bash
git clone https://github.com/abhishekkunal51/member-display-tool.git
cd member-display-tool
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Unix/macOS
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line

```bash
# Display names from default file (members.csv)
python display_names.py

# Display names from a specific file
python display_names.py path/to/your/file.csv
```

### MCP Server

The MCP server allows Claude to interact with your member data directly.

**Available Tools:**
- `list_members` - List members with pagination
- `search_members` - Search by name or email
- `get_member_by_id` - Get specific member details
- `get_member_count` - Get total member count
- `get_members_by_gender` - Filter members by gender
- `get_gender_statistics` - Get gender distribution stats

**Run the MCP server:**
```bash
python mcp_server.py
```

**Configure with Claude Desktop:**

Add to your Claude Desktop config (`claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "member-display-tool": {
      "command": "python",
      "args": ["mcp_server.py"],
      "cwd": "/path/to/member-display-tool"
    }
  }
}
```

## CSV Format

Your CSV file must include these columns:
- `first_name`
- `last_name`

Example:
```csv
id,first_name,last_name,email
1,John,Doe,john@example.com
2,Jane,Smith,jane@example.com
```

## Error Handling

The script handles:
- File not found
- Empty files
- Missing required columns
- CSV parsing errors
- Encoding issues
- Permission errors

## Exit Codes

| Code | Description |
|------|-------------|
| 0    | Success     |
| 1    | Error       |
