
import os
import requests
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI(title="SearchWise")

app.mount("/static", StaticFiles(directory="static"), name="static")


class SearchRequest(BaseModel):
    query: str


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.post("/api/search")
def search(request: SearchRequest):
    query = request.query.strip()

    if not query:
        raise HTTPException(
            status_code=400,
            detail="Please enter a search query."
        )

    api_key = os.getenv("SERPAPI_KEY")

    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="SerpApi key is not configured."
        )

    try:
        response = requests.get(
            "https://serpapi.com/search.json",
            params={
                "engine": "google",
                "q": query,
                "api_key": api_key,
            },
            timeout=20,
        )
        response.raise_for_status()
        data = response.json()

    except requests.RequestException:
        raise HTTPException(
            status_code=502,
            detail="Search service unavailable. Please try again."
        )

    results = []

    for item in data.get("organic_results", [])[:8]:
        results.append({
            "title": item.get("title", "Untitled"),
            "link": item.get("link", ""),
            "snippet": item.get(
                "snippet", "No description available."
            ),
        })

    
    from urllib.parse import urlparse

    websites = set()

    for item in results:
        link = item.get("link", "")
        domain = urlparse(link).netloc.lower()

        if domain.startswith("www."):
            domain = domain[4:]

        if domain:
            websites.add(domain)

    return {
        "query": query,
        "results": results,
        "total_results_returned": len(results),
        "unique_websites": len(websites),
        "website_names": sorted(websites),
    }

