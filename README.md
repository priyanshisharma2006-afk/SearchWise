
# 🔎 SearchWise — Search Smarter, Research Better

SearchWise is a lightweight, web-based research tool that helps users explore topics through search results from multiple websites. It presents relevant links, short descriptions, and a source overview in one simple interface.

## ✨ Features

- **Web Search:** Search for information on any topic.
- **Clear Results:** View result titles, descriptions, and clickable links.
- **Source Overview:** See the number of results returned and how many unique websites they come from.
- **Simple Interface:** A clean, beginner-friendly web experience.
- **FastAPI Backend:** Handles search requests through a REST API.
- **Error Handling:** Provides useful messages when a search fails or the service is unavailable.

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, FastAPI
- **Search API:** SerpApi
- **Server:** Uvicorn

## 📁 Project Structure

```text
Serpai/
├── main.py
├── test_serpapi.py
├── README.md
└── static/
    └── index.html
```

## ⚙️ Getting Started

### Prerequisites

- Python 3.10 or newer
- A SerpApi account and API key
- pip

### 1. Clone or download the project

If you have the project on GitHub:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Serpai
```

Alternatively, open your downloaded project folder in a terminal.

### 2. Install dependencies

```bash
python -m pip install fastapi uvicorn requests
```

### 3. Configure your API key

Set your SerpApi key as an environment variable.

**Windows Command Prompt:**

```bat
set "SERPAPI_KEY=YOUR_SERPAPI_API_KEY"
```

Replace `YOUR_SERPAPI_API_KEY` with your actual key. Do not share your key or commit it to GitHub.

### 4. Start the application

```bash
python -m uvicorn main:app --reload
```

### 5. Open SearchWise

Visit the following address in your browser:

http://127.0.0.1:8000

## 🔌 API Endpoint

### `POST /api/search`

Accepts a search query and returns search results and source information.

**Example request:**

```json
{
  "query": "How does solar energy work?"
}
```

**Response structure:**

```json
{
  "query": "How does solar energy work?",
  "results": [
    {
      "title": "Example result",
      "link": "https://example.com",
      "snippet": "A short description of the result."
    }
  ],
  "total_results_returned": 1,
  "unique_websites": 1,
  "website_names": [
    "example.com"
  ]
}
```

*The example above illustrates the response structure; actual results depend on the search query.*

Interactive API documentation is available at:

http://127.0.0.1:8000/docs

## 🔐 Security Notes

- Keep your SerpApi key private.
- Never commit API keys or other secrets to version control.
- Do not expose your API key in frontend JavaScript or HTML.
- Review the search results and verify information using the original sources.

## 🚀 Future Improvements

- Summarize search results into a concise research snapshot.
- Add filters for domains and result types.
- Improve source comparison and research organization.
- Add automated tests and deployment support.

## 👩‍💻 Project Goal

SearchWise aims to make exploring online information simpler by bringing search results and source diversity into one accessible interface.

---

**Built with Python, FastAPI, and SerpApi.**
