from fastapi import FastAPI
from fastapi.middleware.cors import (
    CORSMiddleware
)

from app.routes.chat import (
    router
)

from app.services.rag_service import (
    index_documents
)

app = FastAPI(
    title="TRUEAILAB RAG Assistant"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.on_event("startup")
def startup_event():

    print(
        "Indexing documents..."
    )

    index_documents()

    print(
        "Documents indexed."
    )


app.include_router(
    router,
    prefix="/api"
)


@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }