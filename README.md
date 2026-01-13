# Member Display Tool

A Python command-line tool for reading and displaying member names from CSV files.

## Features

- Read member data from CSV files
- Display formatted full names (first + last name)
- Comprehensive error handling
- Command-line argument support
- Shows total member count

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/MY_AWESOME_PROJECT.git
cd MY_AWESOME_PROJECT
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

```bash
# Display names from default file (members.csv)
python display_names.py

# Display names from a specific file
python display_names.py path/to/your/file.csv
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
