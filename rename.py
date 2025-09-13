import os
import re

folder = r"C:\Users\Gateway_Security\Pictures\Accenture\Accenture 2"

for filename in os.listdir(folder):
    if filename.lower().endswith(".jpg"):
        name, ext = os.path.splitext(filename)

        # Normalize spaces
        clean_name = re.sub(r"\s+", " ", name.strip())
        parts = clean_name.split(" ")

        if len(parts) >= 2:
            surname = parts[-1]
            given_names = " ".join(parts[:-1])
            new_name = f"{surname} {given_names}{ext}"

            old_path = os.path.join(folder, filename)
            new_path = os.path.join(folder, new_name)

            # Handle duplicates
            counter = 1
            while os.path.exists(new_path):
                new_name = f"{surname} {given_names} ({counter}){ext}"
                new_path = os.path.join(folder, new_name)
                counter += 1

            os.rename(old_path, new_path)
            print(f"Renamed: {filename} → {new_name}")
