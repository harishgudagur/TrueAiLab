import json

from app.utils.chunker import (
    chunk_text
)

from app.services.embedding_service import (
    get_embedding
)

from app.vectorstore.faiss_store import (
    add_vector
)


def index_documents():

    with open(
        "docs.json",
        "r",
        encoding="utf-8"
    ) as file:

        docs = json.load(file)

    for document in docs:

        title = document["title"]
        content = document["content"]

        chunks = chunk_text(content)

        for idx, chunk in enumerate(chunks):

            embedding = get_embedding(
                chunk
            )

            metadata = {
                "title": title,
                "chunk_id": idx,
                "source_document": title,
                "chunk": chunk
            }

            add_vector(
                embedding,
                metadata
            )