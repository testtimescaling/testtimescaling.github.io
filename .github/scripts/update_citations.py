import json
import requests
import time

headers = {
    "User-Agent": "Citation-Badge-Updater"
}

def arxiv_to_doi(arxiv_id):
    url = f"https://api.semanticscholar.org/graph/v1/paper/arXiv:{arxiv_id}?fields=externalIds"
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        data = r.json()
        doi = data.get("externalIds", {}).get("DOI")
        return doi
    return None

def get_citation_count(doi):
    if not doi:
        return 0
    url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}?fields=citationCount"
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.json().get("citationCount", 0)
    return 0

def generate_svg(count):
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="160" height="30">
  <rect width="160" height="30" fill="#4c1"/>
  <text x="10" y="20" fill="white" font-family="Arial" font-size="14">
    Citations: {count}
  </text>
</svg>
""".strip()

def main():
    with open("papers.json", "r") as f:
        papers = json.load(f)

    total_citations = 0
    for p in papers:
        arxiv_id = p["arxiv_id"]
        print(f"📘 Fetching DOI for arXiv:{arxiv_id}")
        doi = arxiv_to_doi(arxiv_id)
        if doi:
            print(f"🔗 Found DOI: {doi}")
        else:
            print("❌ DOI not found, skipping.")
            continue

        count = get_citation_count(doi)
        print(f"📊 Citations: {count}")
        total_citations += count

        time.sleep(1)  # Respect rate limit

    svg = generate_svg(total_citations)
    with open("citation-badge.svg", "w") as f:
        f.write(svg)

    print(f"✅ Total citations: {total_citations}")

if __name__ == "__main__":
    main()
