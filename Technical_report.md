# HybridRAG-Pro  
## Production-Ready Retrieval-Augmented Generation System

---

## 1. Overview

HybridRAG-Pro is a production-grade Retrieval-Augmented Generation (RAG) system designed to answer complex, domain-specific queries over structured, multi-document datasets. The system focuses on retrieval quality optimization through advanced chunking strategies, hybrid dense+sparse retrieval, and cross-encoder reranking.

Unlike basic RAG implementations that rely solely on vector similarity, this system integrates multiple retrieval strategies and metadata-aware indexing to improve precision, grounding, and explainability.

---

## 2. System Architecture

**Pipeline Flow:**

User Query  
→ Hybrid Retrieval (Dense + Sparse)  
→ Top 25 Candidates  
→ Cross-Encoder Reranking  
→ Top 5 Context Chunks  
→ LLM Generation  
→ Final Answer + Source Metadata  

### Core Components

- **Embedding Model:** `text-embedding-3-small`
- **Vector Database:** Pinecone (Serverless, cosine similarity)
- **Sparse Retrieval:** BM25
- **Reranker:** `BAAI/bge-reranker-base`
- **LLM:** GPT-4o-mini
- **Frontend:** Streamlit

Each stored chunk contains structured metadata:

- `source`
- `page`
- `section`
- `chunk_id`

This ensures traceability and transparent citation display.

---

## 3. Advanced Chunking Strategy Comparison

Two chunking strategies were implemented and evaluated.

### Strategy A: Fixed-Size Chunking

- 512 tokens
- 100 token overlap

**Advantages:**
- Simple implementation
- Strong recall
- Stable chunk size

**Limitations:**
- May split semantic boundaries
- Sometimes mixes unrelated subtopics

---

### Strategy B: Parent-Document Retrieval (Small Indexed Chunks)

- 200-token chunks indexed
- Parent-level context preserved through metadata
- More semantically focused segments

**Advantages:**
- Better semantic coherence
- Higher precision retrieval
- Cleaner reranking input

**Result:**

Parent-document chunking produced more focused candidate sets and improved downstream reranking effectiveness. It reduced irrelevant context and improved answer clarity for technical comparison queries.

---

## 4. Hybrid Retrieval Strategy

The system combines:

- **Dense Retrieval** (semantic similarity via embeddings)
- **Sparse Retrieval** (BM25 keyword matching)

Hybrid scoring function:
