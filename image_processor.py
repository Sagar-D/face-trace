from insightface.app import FaceAnalysis
import cv2

face_recognizer = FaceAnalysis(name="buffalo_l")
face_recognizer.prepare(ctx_id=0, det_size=(640,640))


def generate_face_embeddings(file_path:str) :
    
    print(f"Reading Photo {file_path}")
    img = cv2.imread(file_path)

    print(f"Generating Face Embeddings for {file_path}")
    faces = face_recognizer.get(img)
    print(f"Detected {len(faces)} faces in the photo {file_path}")

    face_embeddings = []
    ids = []
    metadatas = []

    for index, face in enumerate(faces):
        face_embeddings.append(face.normed_embedding)
        metadatas.append(
            {
                "bbox": ",".join([str(point) for point in face.bbox]),
                "file_path": file_path
            }
        )
        ids.append(f"{file_path}_{str(index)}")
    
    return face_embeddings, ids, metadatas