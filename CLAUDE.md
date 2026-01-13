# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Python project for reading and displaying member data from CSV files. The project processes member records and outputs formatted name lists with comprehensive error handling.

## Project Structure

```
MY_AWESOME_PROJECT/
├── display_names.py    # Main script with error handling (production-ready)
├── display_members.py  # Simple script (basic version)
├── members.csv         # Sample data file (1000 member records)
├── venv/               # Python virtual environment
└── CLAUDE.md           # This file
```

## Running Scripts

```bash
# Display all member names from default file (members.csv)
python display_names.py

# Display names from a specific CSV file
python display_names.py path/to/file.csv
```

## Environment Setup

```bash
# Activate virtual environment
# Windows:
venv\Scripts\activate

# Unix/macOS:
source venv/bin/activate
```

## Data Format

The CSV files must contain the following required columns:
- `first_name` - Member's first name
- `last_name` - Member's last name

Optional columns (present in members.csv):
- `id` - Unique identifier
- `email` - Email address
- `gender` - Gender field
- `ip_address` - IP address

Example CSV format:
```csv
id,first_name,last_name,email,gender,ip_address
1,John,Doe,john@example.com,Male,192.168.1.1
```

## Error Handling

The `display_names.py` script handles the following error conditions:
- File not found
- Empty file
- Missing required columns (`first_name`, `last_name`)
- CSV parsing errors
- File encoding issues (expects UTF-8)
- Permission denied errors
- Empty name values (warns but continues)

## Exit Codes

- `0` - Success
- `1` - Error occurred

## Key Functions

### `display_names(filename)`
Main function that reads a CSV file and prints all member names.

**Parameters:**
- `filename` (str): Path to the CSV file

**Returns:**
- `True` on success
- `False` on error

## Dependencies

- Python 3.x (standard library only)
- Uses built-in modules: `csv`, `sys`, `os`
