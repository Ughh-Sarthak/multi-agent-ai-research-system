# 🔍 Multi-Agent AI Research System

A multi-agent pipeline that autonomously searches the web, scrapes content, writes a structured research report, and critiques it — all powered by Mistral AI and LangChain.

---

## 🧠 System Architecture

```
User Topic Input
      │
      ▼
pipeline.py (Orchestrator)
      │
      ├──► Search Agent (build_search_agent)
      │         └── Tavily web_search tool → Top 5 results
      │
      ├──► Reader Agent (build_reader_agent)
      │         └── BeautifulSoup scrape_url tool → 3000 chars of content
      │
      ├──► Writer Chain
      │         └── writer_prompt | Mistral LLM | StrOutputParser → Report
      │
      └──► Critic Chain
                └── critic_prompt | Mistral LLM | StrOutputParser → Score + Feedback
```

---

## 📁 Project Structure

```
multiagent/
├── agents.py          # Defines search agent, reader agent, writer chain, critic chain
├── pipeline.py        # Orchestrates the full research pipeline
├── tools.py           # web_search (Tavily) and scrape_url (BeautifulSoup) tools
├── server.py          # FastAPI backend serving the UI and /api/run endpoint
├── main.html          # Frontend UI (dark theme, live pipeline visualization)
├── requirements.txt   # Python dependencies
├── Procfile           # Railway deployment config
└── .env               # API keys (not committed)
```

---

## ⚙️ How It Works

### Step 1 — Search Agent
Uses LangChain's `create_agent` with `ChatMistralAI` and the Tavily `web_search` tool. Fetches top 5 results with titles, URLs, and content snippets for the given topic.

### Step 2 — Reader Agent
Another Mistral-powered agent with the `scrape_url` tool. Selects the most relevant URL from search results and extracts up to 3000 characters of clean text using BeautifulSoup.

### Step 3 — Writer Chain
A LangChain LCEL chain: `writer_prompt | llm | StrOutputParser`. Combines search results and scraped content into a structured report with Introduction, Key Findings, Conclusion, and Sources.

### Step 4 — Critic Chain
Another LCEL chain that reviews the generated report. Returns a score out of 10, Strengths, Areas to Improve, and a one-line verdict.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Ughh-Sarthak/multi-agent-ai-research-system.git
cd multi-agent-ai-research-system
```

### 2. Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root directory:
```
MISTRAL_AI_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Get your keys:
- Mistral AI: https://console.mistral.ai
- Tavily: https://tavily.com

### 5. Run the server
```bash
uvicorn server:app --reload
```

### 6. Open the UI
Visit `http://localhost:8000` in your browser, enter a research topic, and click **Run Pipeline**.

---

## 🌐 Deployment

This project is deployed on **Railway**.

To deploy your own instance:
1. Push the repo to GitHub
2. Connect it to [Railway](https://railway.app)
3. Add environment variables (`MISTRAL_AI_KEY`, `TAVILY_API_KEY`) in the Railway dashboard
4. Railway uses the `Procfile` to start the server automatically:
```
web: uvicorn server:app --host 0.0.0.0 --port $PORT
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| LLM | Mistral AI (`mistral-small-latest`) |
| Agent Framework | LangChain + LangGraph |
| Web Search | Tavily API |
| Web Scraping | BeautifulSoup4 + Requests |
| Backend | FastAPI + Uvicorn |
| Frontend | HTML + CSS + Vanilla JS |
| Deployment | Railway |

---

## 📄 License

MIT License — free for personal and educational use.
