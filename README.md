# Automatic File Sorter

## Project Overview
The **Automatic File Sorter** project is a Python script designed to automatically organize files on your desktop into specific folders based on their file types. This tool helps keep your desktop clutter-free by sorting files into categories such as documents, images, videos, and more.

## Tools Used
- **Python**: Programming language used to create the script.

## Project Steps

### 1. Define File Categories
- Specified the file categories and their corresponding extensions. Examples include:
  - **Documents**: `.pdf`, `.docx`, `.txt`
  - **Images**: `.jpg`, `.png`, `.gif`
  - **Videos**: `.mp4`, `.avi`, `.mov`
  - **Music**: `.mp3`, `.wav`
  - **Archives**: `.zip`, `.rar`

### 2. Script Development
- Wrote a Python script to:
  - Scan the desktop directory for files.
  - Identify each file's type based on its extension.
  - Move each file to its respective folder.
- Used Python's built-in libraries for file handling and manipulation.

### 3. Directory Creation
- Ensured the script checks for the existence of target directories (e.g., "Documents", "Images") and creates them if they do not exist.

### 4. File Moving Logic
- Implemented logic to move files from the desktop to their designated folders.
- Included error handling to manage potential issues, such as file permission errors or already existing files.

### 5. Script Execution
- Provided instructions to run the script and achieve automatic sorting:
  - Save the script file (`file_sorter.py`) on your desktop.
  - Run the script using a Python interpreter.

## Repository Structure
- `AUTOMATED FILE SORTER.py`: The Python script that performs the automatic file sorting.
- `README.md`: Project description and overview.

## Conclusion
This project provides a simple yet effective solution for organizing files on your desktop. By using Python to automate the file sorting process, you can maintain a tidy and organized workspace with minimal effort.

---

Feel free to contribute to this project by suggesting improvements, reporting issues, or submitting pull requests. Happy sorting!
