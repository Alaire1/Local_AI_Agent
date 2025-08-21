# Local AI Restaurant Advisor

This project is a simple AI-powered restaurant advisor that answers user questions based on real restaurant reviews. It uses **LangChain**, **Ollama**, and **Chroma** for building a retrieval-augmented generation (RAG) pipeline.

---

##  Features
- **Local AI Model**: Runs on Ollama with LLaMA model.
- **Vector Search**: Uses Chroma to store and retrieve restaurant review embeddings.
- **Interactive Q&A**: Allows users to ask multiple questions in a conversational manner.
- **Contextual Memory**: Maintains recent conversation history for better responses.
- **Data Grounding**: Answers strictly based on provided reviews, reducing hallucinations.

---

## Tech Stack
- **Python**
- **LangChain** – for building the LLM pipeline.
- **Ollama** – local LLM inference.
- **Chroma** – vector database for storing and retrieving embeddings.
- **Pandas** – for reading the reviews dataset.
