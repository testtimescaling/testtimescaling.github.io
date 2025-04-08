import json
import requests

def fetch_citation_count(arxiv_id):
    url = f"https://api.semanticscholar.org/graph/v1/paper/arXiv:{arxiv_id}?fields=citationCount"
    r = requests.get(url)
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

    total_citations = sum(fetch_citation_count(p['arxiv_id']) for p in papers)

    svg_content = generate_svg(total_citations)
    with open("citation-badge.svg", "w") as f:
        f.write(svg_content)

    print(f"✅ Total citations: {total_citations}")

if __name__ == "__main__":
    main()
