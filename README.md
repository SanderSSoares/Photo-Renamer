# Photo Renamer – Python Utility

A lightweight Python script to **standardize staff photo filenames** into a consistent `Surname GivenNames.jpg` format.  
Useful for access systems, HR directories, or any environment where consistent file naming is important.

---

## Features
- Automatically renames `.jpg` files in a chosen folder
- Converts names like:
  - `John Doe.jpg` → `Doe John.jpg`
  - `Jane Mary Smith.jpg` → `Smith Jane Mary.jpg`
- Normalizes extra spaces in filenames
- Handles duplicate names by adding a counter, e.g., `Doe John (1).jpg`

---

## Requirements
- Python 3.7+
- Standard library only (no extra dependencies)

---

## Usage
1. Edit the `folder` variable inside `rename.py` to point to your photo directory:

---

## Author
**Sander Soares**  
BSc (Hons) in Computing IT | Networking & Cloud Enthusiast  

---

```python
folder = r"C:\Users\YourName\Pictures\Photos"

