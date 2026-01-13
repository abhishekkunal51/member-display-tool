import csv
import sys
import os

def display_names(filename):
    # Check if file exists
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return False

    # Check if file is empty
    if os.path.getsize(filename) == 0:
        print(f"Error: File '{filename}' is empty.")
        return False

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            # Check if required columns exist
            if reader.fieldnames is None:
                print("Error: Could not read CSV headers.")
                return False

            required_columns = ['first_name', 'last_name']
            missing_columns = [col for col in required_columns if col not in reader.fieldnames]

            if missing_columns:
                print(f"Error: Missing required columns: {', '.join(missing_columns)}")
                print(f"Available columns: {', '.join(reader.fieldnames)}")
                return False

            # Display names
            count = 0
            for row in reader:
                first_name = row['first_name'].strip() if row['first_name'] else ''
                last_name = row['last_name'].strip() if row['last_name'] else ''

                if first_name or last_name:
                    print(f"{first_name} {last_name}")
                    count += 1
                else:
                    print(f"Warning: Empty name found at row {count + 2}")

            print(f"\nTotal members displayed: {count}")
            return True

    except csv.Error as e:
        print(f"Error: CSV parsing error - {e}")
        return False
    except UnicodeDecodeError:
        print("Error: File encoding issue. Try a different encoding.")
        return False
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
        return False
    except Exception as e:
        print(f"Error: Unexpected error - {e}")
        return False

if __name__ == "__main__":
    # Allow filename as command-line argument
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "members.csv"

    success = display_names(filename)
    sys.exit(0 if success else 1)
