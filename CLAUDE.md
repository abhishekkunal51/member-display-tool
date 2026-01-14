# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Python project for reading and displaying member data from CSV files. Includes an MCP server for AI integration.

## Running Scripts

```bash
# Display member names
python display_names.py

# Display names from specific file
python display_names.py path/to/file.csv

# Run MCP server
python mcp_server.py
```

## MCP Server

The `mcp_server.py` provides these tools for Claude integration:

| Tool | Description |
|------|-------------|
| `list_members` | List members with pagination (limit, offset) |
| `search_members` | Search by name or email |
| `get_member_by_id` | Get member details by ID |
| `get_member_count` | Get total member count |
| `get_members_by_gender` | Filter by gender |
| `get_gender_statistics` | Gender distribution stats |

## Data Format

Required CSV columns: `first_name`, `last_name`

Optional: `id`, `email`, `gender`, `ip_address`

## Dependencies

- Python 3.x
- `mcp[cli]>=1.0.0` (for MCP server)

## Key Files

- `display_names.py` - CLI tool with error handling
- `mcp_server.py` - MCP server implementation
- `members.csv` - Sample data (1000 records)
