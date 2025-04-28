import httpx
import os
from dotenv import load_dotenv
import subprocess
import json

load_dotenv()
BRAVE_API_KEY = os.getenv("BRAVE_API_KEY")
BRAVE_SEARCH_URL = "https://api.search.brave.com/res/v1/web/search"

async def search_pdfs(prompt: str):
    query = f"filetype:pdf {prompt}"

    headers = {
        "Accept": "application/json",
        "X-Subscription-Token": BRAVE_API_KEY
    }
    params = {
        "q": query,
        "count": 5,
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(BRAVE_SEARCH_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

    results = []
    for item in data.get("web", {}).get("results", []):
        results.append({
            "title": item.get("title"),
            "url": item.get("url"),
        })
    return results

# 代替実装: curlを使用した検索（必要な場合のみ使用）
def search_pdfs_with_curl(prompt: str):
    query = f"filetype:pdf {prompt}"
    curl_command = [
        "curl",
        "-X", "GET",
        "-H", "Accept: application/json",
        "-H", "Accept-Encoding: gzip",
        "-H", f"X-Subscription-Token: {BRAVE_API_KEY}",
        f"{BRAVE_SEARCH_URL}?q={query}&count=5"
    ]
    
    result = subprocess.run(curl_command, capture_output=True, text=True)
    data = json.loads(result.stdout)
    
    results = []
    for item in data.get("web", {}).get("results", []):
        results.append({
            "title": item.get("title"),
            "url": item.get("url"),
        })
    return results
