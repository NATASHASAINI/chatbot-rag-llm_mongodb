# 🤖 RAG Chatbot with LLM & MongoDB Atlas

A Retrieval-Augmented Generation (RAG) chatbot built with Sentence Transformers, MongoDB Atlas Vector Search, and OpenAI GPT. Designed as a Discord Q&A assistant that answers questions using a custom knowledge base.

---

## 🧠 Architecture

```
User Query
    │
    ▼
Embed Query (Sentence Transformers: all-MiniLM-L6-v2)
    │
    ▼
Vector Search (MongoDB Atlas Vector Search)
    │
    ▼
Retrieve Top-K Relevant Chunks
    │
    ▼
Augment Prompt + Send to LLM (OpenAI GPT-3.5-turbo)
    │
    ▼
Return Answer to User
```

---

## ✨ Features

- **Data Ingestion Pipeline** — loads a Discord chat dataset from HuggingFace, chunks text with sliding window overlap, and stores in MongoDB
- **Semantic Embeddings** — uses `all-MiniLM-L6-v2` from Sentence Transformers for dense vector representations
- **Vector Search** — MongoDB Atlas Vector Search with cosine similarity for relevant chunk retrieval
- **RAG Chain** — combines retrieved context with user query and sends to OpenAI GPT for answer generation
- **Conversational Memory** — maintains message history for multi-turn chat

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Embeddings | Sentence Transformers (`all-MiniLM-L6-v2`) |
| Vector Store | MongoDB Atlas Vector Search |
| LLM | OpenAI GPT-3.5-turbo |
| Dataset | HuggingFace `breadlicker45/discord-chat` |
| Language | Python 3.9+ |

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/NATASHASAINI/chatbot-rag-llm_mongodb.git
cd chatbot-rag-llm_mongodb
```

### 2. Install dependencies
```bash
pip install datasets pandas pymongo sentence_transformers openai scikit-learn numpy accelerate
```

### 3. Set up environment variables

Create a `.env` file in the root directory:
```
MONGODB_URI=mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/?appName=Cluster0
OPENAI_API_KEY=sk-...
```

> ⚠️ **Never commit your `.env` file or hardcode credentials.** The `.gitignore` in this repo excludes `.env` automatically.

### 4. Set up MongoDB Atlas Vector Search Index

In your MongoDB Atlas dashboard, create a Vector Search index on the `chatbot.embeddings` collection:
```json
{
  "fields": [
    {
      "type": "vector",
      "path": "embedding",
      "numDimensions": 384,
      "similarity": "cosine"
    }
  ]
}
```

### 5. Run the notebook
Open `chatbot_rag_llm_mongodb.ipynb` in Jupyter or Google Colab and run all cells in order.

---

## 📁 Project Structure

```
chatbot-rag-llm_mongodb/
│
├── chatbot_rag_llm_mongodb.ipynb   # Main notebook: ingestion, retrieval, RAG chain
├── README.md                        # Project documentation
├── .gitignore                       # Excludes .env, credentials, checkpoints
└── .env.example                     # Template for environment variables
```

---

## 📊 How It Works

### Step 1 — Data Ingestion
- Loads `breadlicker45/discord-chat` dataset from HuggingFace
- Chunks each document into 500-character windows with 50-character overlap
- Stores chunked documents in MongoDB Atlas

### Step 2 — Embedding & Retrieval
- Encodes the user query using `all-MiniLM-L6-v2`
- Performs cosine similarity search across all chunk embeddings
- Returns the top-5 most relevant chunks

### Step 3 — Answer Generation
- Combines the user query + retrieved chunks into a structured prompt
- Sends the augmented prompt to OpenAI GPT-3.5-turbo
- Returns the generated answer to the user

---

## 🔐 Security Note

This project uses environment variables for all sensitive credentials. **Do not hardcode** MongoDB URIs or OpenAI API keys in your code. Use `.env` files locally and secret managers in production.

---

## 📄 License

MIT License — feel free to use and modify.

---

## 👩‍💻 Author

**Natasha Saini** — [LinkedIn](https://www.linkedin.com/in/natasha-saini-72a6711b9/) | [GitHub](https://github.com/NATASHASAINI)
