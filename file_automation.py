# CodeAlpha - Task Automation Script
# Move all .jpg files from one folder to another

import os
import shutil

source_folder = "source_folder"
destination_folder = "destination_folder"

# Create destination folder if not exists
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Move all .jpg files
for filename in os.listdir(source_folder):
    if filename.endswith(".jpg"):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename}")

print("All .jpg files moved successfully.")