import os
import shutil

def scan_directory_for_photos(folder: str):

    extensions = (".jpg", ".jpeg", ".png")
    image_files = []

    print(f"Scanning Folder for photos - {folder}")
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(extensions):
                image_files.append(os.path.join(root, file))

    print(f"Found {len(image_files)} photos")

    return image_files

def copy_photos_to_folder(photos:list[str], folder:str) :

    os.makedirs(name=folder, exist_ok=True)
    for photo in photos :
        shutil.copy2(photo, folder)
    
    print(f"Photos successfully copied to new location {folder}")

