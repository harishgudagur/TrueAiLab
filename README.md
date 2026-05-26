# TRUEAILAB RAG Assistant

## Features

- FastAPI Backend
- Retrieval-Augmented Generation (RAG)
- Sentence Transformer Embeddings
- FAISS Vector Similarity Search
- Knowledge Base Retrieval
- Conversation Memory
- Frontend Chat UI

## Tech Stack

- FastAPI
- Python
- Sentence Transformers
- FAISS
- HTML/CSS/JavaScript

## Architecture

User Query
↓
Generate Embedding
↓
FAISS Similarity Search
↓
Retrieve Relevant Chunks
↓
Generate Context-Based Response
↓
Return Answer

## Run Project

Backend:

```bash
uvicorn main:app --reload