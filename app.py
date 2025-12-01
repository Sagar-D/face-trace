from image_processor import generate_face_embeddings
from vector_store_manager import add_faces_to_collection, get_face_matching_photos, collection
from file_handler import scan_directory_for_photos, copy_photos_to_folder
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--scan-dir", dest="directory", help="Directory / Folder to scan for new photos", default="")
args = parser.parse_args()

scan_folder = False
photos_dir = ""
if args.directory and type(args.directory) == str and args.directory.strip() != "" :
    scan_folder = True
    photos_dir = args.directory.strip()


if scan_folder and photos_dir.strip() != "" :
    image_files = scan_directory_for_photos(photos_dir)
    for image_file in image_files :
        print(f"Creating embeddings and storing to db for {image_file}")    
        face_embeddings, ids, metadatas = generate_face_embeddings(image_file)
        add_faces_to_collection(face_embeddings,ids,metadatas)


print("--"*30)
print(f"Total number of face embeddings in collection - {collection.count()}")
print("--"*30)


while True :
    print("Upload a single face image to find the matches")
    face_file = input("Facial Image Path : ")
    face_embeddings, ids, metadatas = generate_face_embeddings(face_file)
    photos = get_face_matching_photos(face_embeddings)

    if photos == None or len(photos) == 0 :
        print("No matching photos found!! Try again with different face!")
        continue

    print(f"\n\nFound {len(photos)} photos matching face\n")
    new_folder = input("Folder to copy the matched photos (Send empty string to skip this step) : ")

    if new_folder.strip() == "" :
        print("Photos were not copied to any new folder. Skipped this step")
    
    copy_photos_to_folder(photos, new_folder)


