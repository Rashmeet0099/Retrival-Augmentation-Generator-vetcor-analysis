# Retrival-Augmentation-Generator-vetcor-analysis

# 🔍 RAG-based PDF Semantic Search with LangChain, Pinecone & Gemini

This project demonstrates how to build a semantic search system using:

- 📄 PDF documents as the data source
- 🔎 Google Gemini Embeddings (`embedding-001`)
- 🧠 LangChain for LLM operations
- 🌲 Pinecone for vector storage and similarity search
- 🧰 LangSmith for debugging & tracing

---

## 🚀 Features

- ✅ Load PDF documents from a remote URL
- ✅ Split and chunk text intelligently with `RecursiveCharacterTextSplitter`
- ✅ Generate semantic embeddings using Google Gemini
- ✅ Store and retrieve using Pinecone vector database (cosine similarity)
- ✅ Query and retrieve top results with similarity scores
- ✅ Batched queries via `@chain` and LangChain core

---

## 📁 Project Structure

