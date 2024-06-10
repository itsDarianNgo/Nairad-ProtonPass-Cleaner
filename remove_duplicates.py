import json
import os
from typing import List, Dict

# Define constants for directories
ORIGINAL_DIR = "original"
CLEANED_DIR = "cleaned"
INPUT_FILENAME = "data.json"
OUTPUT_FILENAME = "cleaned_data.json"


# Define a function to load JSON data from a file
def load_json(file_path: str) -> Dict:
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


# Define a function to save JSON data to a file
def save_json(file_path: str, data: Dict):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


# Define a function to remove duplicates for login items only
def remove_duplicates(data: Dict) -> Dict:
    seen_entries = set()
    cleaned_vaults = {}
    duplicate_count = 0
    skipped_count = (
        0  # Count of entries skipped due to missing fields or non-login type
    )

    for vault_id, vault in data["vaults"].items():
        unique_items = []
        for item in vault["items"]:
            # Process only login items
            if item["data"].get("type") != "login":
                unique_items.append(item)
                continue

            content = item.get("data", {}).get("content", {})
            username = content.get("username")
            password = content.get("password")

            # Check if the necessary fields are present
            if username is None or password is None:
                skipped_count += 1
                unique_items.append(item)  # Keep non-login or incomplete entries as-is
                continue

            # Create a unique identifier for each login entry based on username and password
            entry_key = (username, password)

            if entry_key not in seen_entries:
                seen_entries.add(entry_key)
                unique_items.append(item)
            else:
                duplicate_count += 1

        # Add cleaned items back to the vault
        cleaned_vaults[vault_id] = {**vault, "items": unique_items}

    print(f"Total duplicates removed: {duplicate_count}")

    return {**data, "vaults": cleaned_vaults}


# Main function to process the JSON file
def main():
    # Construct input and output file paths
    input_file_path = os.path.join(ORIGINAL_DIR, INPUT_FILENAME)
    output_file_path = os.path.join(CLEANED_DIR, OUTPUT_FILENAME)

    # Ensure the output directory exists
    os.makedirs(CLEANED_DIR, exist_ok=True)

    # Load the JSON data
    data = load_json(input_file_path)

    # Remove duplicates and keep one instance
    cleaned_data = remove_duplicates(data)

    # Save the cleaned data
    save_json(output_file_path, cleaned_data)

    print(f"Duplicates removed and cleaned data saved to {output_file_path}")


# Run the main function
if __name__ == "__main__":
    main()
