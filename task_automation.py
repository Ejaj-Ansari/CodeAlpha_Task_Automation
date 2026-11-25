import os
import shutil

# Current project folder
source_folder = os.getcwd()

# Destination folder
destination_folder = os.path.join(source_folder, "JPG_Files")

# Create destination folder
os.makedirs(destination_folder, exist_ok=True)

# Check all files
for file_name in os.listdir(source_folder):

    # Detect both JPG and JPEG files
    if file_name.lower().endswith((".jpg", ".jpeg")):

        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)

        # Move the image
        shutil.move(source_path, destination_path)

        print(f"Moved: {file_name}")

print("\nJPG file organization completed!")