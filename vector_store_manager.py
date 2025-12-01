import chromadb
from chromadb import Settings
import constants

vector_db = chromadb.Client(settings=Settings(persist_directory="face_vectors"))
collection = vector_db.get_or_create_collection(
    name="face_classify_test", metadata={"hnsw:space": "cosine"}
)


def add_faces_to_collection(face_embeddings: list, ids: list, metadatas: list):

    print(f"Adding {len(ids)} face embeddings to Vector store")
    collection.add(ids=ids, embeddings=face_embeddings, metadatas=metadatas)


def get_face_matching_photos(query_embedding: list):

    query_results = collection.query(
        query_embeddings=query_embedding, n_results=constants.FACE_QUERY_TOP_K
    )

    photos = set()
    for metadata, distance in zip(
        query_results["metadatas"][0], query_results["distances"][0]
    ):
        if float(distance) > float(constants.MAX_DISTANCE_FOR_SIMILAR_FACE):
            break
        photos.add(metadata["file_path"])

    return photos
