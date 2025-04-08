import json
import requests
import time

headers = {"User-Agent": "Citation-Updater"}

def arxiv_to_doi(arxiv_id):
    url = f"https://api.semanticscholar.org/graph/v1/paper/arXiv:{arxiv_id}?fields=externalIds"
    res = requests.get(url, headers=headers)
    if res.ok:
        return res.json().get("externalIds", {}).get("DOI")
    return None

def get_citations(doi):
    if not doi: return 0
    url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}?fields=citationCount"
    res = requests.get(url, headers=headers)
    if res.ok:
        return res.json().get("citationCount", 0)
    return 0

def generate_svg(count):
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="160" height="30">
  <rect width="160" height="30" fill="#007acc"/>
  <text x="10" y="20" fill="#fff" font-family="Arial" font-size="14">
    Citations: {count}
  </text>
</svg>
"""

def main():
    
    total = 0
    arxiv_id = "2503.24235"
    doi = arxiv_to_doi(arxiv_id)
    if doi:
        count = get_citations(doi)
        print(f"{arxiv_id} => {count} citations")
        total += count
    time.sleep(1)

    with open("citation-badge.svg", "w") as f:
        f.write(generate_svg(total))
    print(f"✅ Total citations: {total}")

if __name__ == "__main__":
    main()
