import os
import re

main_folder = os.getcwd()  # Automatically picks current directory

for item in os.listdir(main_folder):
    item_path = os.path.join(main_folder, item)

    match = re.match(r"M([1-9])-(.+)", item)
    if os.path.isdir(item_path) and match:
        new_name = f"M0{match.group(1)}-{match.group(2)}"
        new_path = os.path.join(main_folder, new_name)

        print(f"Renaming: {item} → {new_name}")
        os.rename(item_path, new_path)

print("✅ Done! All folders renamed.")