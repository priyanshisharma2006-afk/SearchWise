import os
import requests

api_key = os.getenv("SERPAPI_KEY")

if not api_key:
    print("API key is missing.")
    raise SystemExit(1)

params = {
    "engine": "google",
    "q": "data science internships India",
    "api_key": api_key
}

response = requests.get(
    "https://serpapi.com/search.json",
    params=params,
    timeout=30
)

print("Status code:", response.status_code)

data = response.json()

if response.status_code == 200:
    print("\nSearch successful!\n")

    for result in data.get("organic_results", [])[:5]:
        print("Title:", result.get("title"))
        print("Link:", result.get("link"))
        print()
else:
    print("Search failed:", data.get("error", "Unknown error"))