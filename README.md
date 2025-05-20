# 🤖 Langchain - Chat & Search Agent

Langchain is an AI-powered chatbot built with **Streamlit**, **LangChain**, and **Groq's Llama3-8B model**, capable of responding to user queries using information from:
- 🔍 DuckDuckGo Search
- 📚 Wikipedia
- 📄 Arxiv Papers

It provides **interactive, streaming responses** and displays **agent thoughts and actions** live inside the app using LangChain's `StreamlitCallbackHandler`.

---

## 🚀 Features

- 🧠 Natural Language Understanding via Llama 3 (8B) from Groq
- 🌐 Real-time web search using DuckDuckGo
- 📖 Wikipedia summaries
- 📄 Arxiv paper summaries
- 💬 Chat memory using `st.session_state`
- 🔁 Agent-driven responses using `ZERO_SHOT_REACT_DESCRIPTION`
- 📟 Live agent actions shown inside the Streamlit interface

---

## 🧱 Tech Stack

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Groq (Llama3)](https://groq.com/)
- [DuckDuckGo Search API](https://duckduckgo.com/)
- [Wikipedia & Arxiv Wrappers (LangChain)](https://python.langchain.com/)
- [HuggingFace Embeddings](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- `.env` configuration for secure API key management

---

## 📂 Project Structure

```
📁 your_project/
├── app.py
├── .env
└── README.md
```

---

## 🔐 .env File Format

Create a `.env` file in your project root and add your API keys:

```
GROQ_API_KEY=your_groq_api_key_here
HF_TOKEN=your_huggingface_token_here
```

---

## ▶️ How to Run

1. **Install dependencies:**
```bash
pip install streamlit langchain langchain-community langchain-groq langchain-huggingface python-dotenv
```

2. **Run the Streamlit app:**
```bash
streamlit run app.py
```

---

## 🧠 How It Works

- The chatbot uses `st.chat_input()` to receive user input.
- Each message is stored in `st.session_state` to maintain memory across re-runs.
- On user query:
  - A new LLM (`ChatGroq`) is initialized.
  - Tools are passed to an agent initialized with `ZERO_SHOT_REACT_DESCRIPTION`.
  - The agent thinks step-by-step, choosing the right tool (search, arxiv, wiki).
  - Live updates are shown using `StreamlitCallbackHandler`.
- The final response is added to the chat and shown in the UI.

---

## ✨ Example Query

```
What are the latest advancements in quantum computing?
```

Agent will:
- Search DuckDuckGo
- Look for Arxiv research papers
- Query Wikipedia
- Merge everything into a natural language answer

---

## 📸 UI Snapshot

> Streamlit chat UI with real-time assistant thinking and responses.
> User inputs appear on the left, assistant responses on the right, with live agent reasoning shown below.

---

## 📃 License

This project is open-sourced for learning and experimentation purposes.

---

## 🙋‍♂️ Questions?

Feel free to raise issues or contact the author.

