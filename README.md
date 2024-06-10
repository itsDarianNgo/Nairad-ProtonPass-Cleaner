# Nairad's ProtonPass Cleaner

A tool to clean duplicate login entries from ProtonPass JSON exports while preserving non-login data.

------

## Features

- **Removes Duplicate Logins**: Cleans up your ProtonPass data by removing duplicate login entries while keeping one instance of each.
- **Preserves Non-Login Data**: Keeps notes, aliases, and other non-login entries untouched.
- **Easy to Use**: Simple setup with clear instructions.
- **Safe and Non-Destructive**: Outputs cleaned data to a separate folder, leaving your original data intact.

## Installation

1. **Clone the Repository**:

   ```
   bashCopy codegit clone https://github.com/itsDarianNgo/Nairad-ProtonPass-Cleaner.git
   cd Nairad-ProtonPass-Cleaner
   ```

2. **Ensure Python is Installed**:

   - Make sure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).

3. **Verify the Required Directory Structure**:

   - Place your ProtonPass export `data.json` file into the `original` folder located next to the script.

## Usage

1. **Navigate to the Project Directory**:

   - Open your terminal.

   - Navigate to the 

     ```
     Nairad-ProtonPass-Cleaner
     ```

      directory where the script is located:

     ```
     bash
     Copy code
     cd path/to/Nairad-ProtonPass-Cleaner
     ```

2. **Run the Script**:

   - Execute the script using Python:

     ```
     bash
     Copy code
     python remove_duplicates.py
     ```

3. **Output**:

   - The cleaned data will be saved to the `cleaned` folder as `cleaned_data.json`.
   - The script will also print the total number of duplicates removed and any entries skipped due to missing fields or being non-login types.

## Example

1. **Original Data Structure**:
   - Place your `data.json` file inside the `original` folder.
   - Example: `original/data.json`
2. **Cleaned Data Structure**:
   - After running the script, the cleaned data will be saved in the `cleaned` folder.
   - Example: `cleaned/cleaned_data.json`

## FAQ

### What is removed by this tool?

- The tool removes duplicate login entries based on their `username` and `password` fields.
- It does **not** remove notes, aliases, or credit card entries.

### How does the tool handle duplicates?

- The script tracks each unique combination of `username` and `password`.
- Only one instance of each unique combination is kept, while duplicates are removed.
- The total number of duplicates removed is reported after the script runs.

### What if I encounter a `KeyError` or a similar issue?

- Ensure that your `data.json` follows the expected ProtonPass export structure.
- If items in your data do not contain `username` or `password` fields, they are skipped and reported.

### Can I change the input and output filenames?

- By default, the script reads from `original/data.json` and writes to `cleaned/cleaned_data.json`.
- You can modify the script to change these paths if needed.

### How can I verify which duplicates were removed?

- The script outputs the number of duplicates removed and the number of entries skipped.
- Review the `cleaned_data.json` file in the `cleaned` folder to see the cleaned list of login entries.

### Can I contribute to this project?

- Absolutely! Feel free to fork the repository and submit a pull request with your improvements.
- Ensure your contributions are well-documented and include test cases if applicable.

## Troubleshooting

### Common Errors

- **FileNotFoundError**: Ensure the `data.json` file is placed correctly in the `original` folder.
- **PermissionError**: Check if you have write permissions for the directories.
- **JSONDecodeError**: Verify that `data.json` is a valid JSON file.

### Additional Help

- Check the Python documentation for any issues related to Python installation or usage.
- Review the script’s comments for insights on how it processes the data.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions, feedback, or help, feel free to reach out via GitHub Issues or contact me on Discord at Cnidarian.