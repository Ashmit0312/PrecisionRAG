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

## 4. Hybrid Retrieval Strategy:


The system combines:

- **Dense Retrieval** (semantic similarity via embeddings)
- **Sparse Retrieval** (BM25 keyword matching)

Hybrid scoring function:
Final Score = α × Dense Score + (1 − α) × Sparse Score


### Why Hybrid?

Dense retrieval captures semantic meaning but may miss:

- Exact acronyms
- Numerical identifiers
- Domain-specific terminology

Sparse retrieval captures exact matches but lacks semantic understanding.

Hybrid search balances both, improving recall and precision in structured datasets.

---

## 5. Reranking for Precision Optimization

After hybrid retrieval, the top 25 candidates are passed to a cross-encoder reranker.

The reranker evaluates each (query, chunk) pair jointly and assigns a strict relevance score. Only the top 5 reranked chunks are passed to the LLM.

### Observed Improvements

Without reranking:
- Semantically similar but contextually irrelevant chunks were included.

With reranking:
- Irrelevant chunks were filtered.
- Context became more focused.
- Answer quality improved significantly for analytical and comparative queries.

Example observation:
A multi-section comparison query initially retrieved loosely related passages. After reranking, only directly relevant sections remained, producing a more structured and accurate response.

---

## 6. Evaluation Methodology

A manual evaluation set of 10 difficult, domain-specific questions was created. The questions required:

- Cross-section reasoning
- Numerical comparisons
- Concept differentiation
- Precise technical references

Evaluation comparisons included:

- Fixed vs Parent chunking
- Dense-only vs Hybrid retrieval
- Hybrid vs Hybrid + Reranker

### Key Findings

- Hybrid retrieval outperformed dense-only retrieval for exact-term queries.
- Reranking significantly improved precision and reduced noise.
- Parent-document chunking improved answer coherence and relevance.

---

## 7. Conclusion

HybridRAG-Pro demonstrates that retrieval optimization is more critical than LLM capability alone in domain-specific RAG systems.

Performance gains were achieved through:

- Structured chunking strategies
- Dense + sparse hybrid retrieval
- Cross-encoder reranking
- Metadata-aware indexing

The system reflects modern enterprise RAG architecture principles and emphasizes retrieval quality, modular design, and evaluation-driven improvement.

---

## Future Improvements

- Query rewriting for improved recall
- Automatic citation highlighting
- Retrieval latency benchmarking
- Adaptive alpha tuning for hybrid weighting
- Automated evaluation metrics (precision@k, MRR)

---
