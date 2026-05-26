from fastapi import (
    APIRouter,
    HTTPException
)

from app.models.schemas import (
    ChatRequest
)

from app.services.embedding_service import (
    get_embedding
)

from app.vectorstore.faiss_store import (
    similarity_search
)

from app.services.llm_service import (
    generate_response
)

from app.services.memory_service import (
    add_message,
    get_history
)

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest):

    if not request.message.strip():
        raise HTTPException(
            status_code=400,
            detail="Message field is required"
        )

    query_embedding = get_embedding(
        request.message
    )

    results = similarity_search(
        query_embedding,
        top_k=3
    )

    threshold = 0.3

    filtered_results = [
        result
        for result in results
        if result["score"] > threshold
    ]

    print(
        "Similarity Scores:",
        [
            r["score"]
            for r in filtered_results
        ]
    )

    if not filtered_results:
        return {
            "reply":
            "I could not find enough information in the knowledge base to answer this question.",
            "tokensUsed": 0,
            "retrievedChunks": 0
        }

    context = "\n".join([
        item["metadata"]["chunk"]
        for item in filtered_results
    ])

    history = get_history(
        request.sessionId
    )

    response = generate_response(
        context=context,
        history=history,
        question=request.message
    )

    add_message(
        request.sessionId,
        "user",
        request.message
    )

    add_message(
        request.sessionId,
        "assistant",
        response["reply"]
    )

    return {
        "reply":
        response["reply"],
        "tokensUsed":
        response["tokens"],
        "retrievedChunks":
        len(filtered_results)
    }