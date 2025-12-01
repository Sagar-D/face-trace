import os


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
