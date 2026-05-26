import faiss
import numpy as np

# MiniLM embedding dimension
dimension = 384

# Cosine similarity
index = faiss.IndexFlatL2(dimension)

stored_chunks = []


def add_vector(vector, metadata):

    vector = np.array(
        [vector]
    ).astype("float32")

    index.add(vector)

    stored_chunks.append(
        metadata
    )


def similarity_search(
    query_vector,
    top_k=3
):

    query_vector = np.array(
        [query_vector]
    ).astype("float32")

    distances, indices = index.search(
        query_vector,
        top_k
    )

    results = []

    for score, idx in zip(
        distances[0],
        indices[0]
    ):

        if idx != -1:
            results.append({
                "score": float(score),
                "metadata":
                stored_chunks[idx]
            })

    return results