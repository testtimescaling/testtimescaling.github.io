import requests
import json

def fetch_arxiv_citation_count(arxiv_id: str) -> int:
    """
    从 Semantic Scholar API 获取指定 arXiv ID 对应的引用数 (citationCount)。
    如果找不到或接口异常，则返回 0。
    """
    url = f"https://api.semanticscholar.org/graph/v1/paper/ARXIV:{arxiv_id}?fields=citationCount"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()
        return data.get("citationCount", 0)
    except Exception as e:
        print(f"[Warning] Failed to fetch citation for ArXiv:{arxiv_id} - {e}")
        return 0

def main():
    # 列出你想要统计引用数的 arXiv ID，可以一个或多个
    # 例如 ["2102.03806", "2102.06828"] 等
    arxiv_ids = [
        "2503.24235",  # 示例
        # "2102.06828",  # 如果还有更多，就继续加
    ]
    
    # 累加所有论文的引用数；你也可以改成分别写不同 JSON
    total_citations = 0
    for aid in arxiv_ids:
        c = fetch_arxiv_citation_count(aid)
        total_citations += c
    
    # 生成供 Shields.io 动态徽章使用的 JSON
    badge_data = {
        "schemaVersion": 1,
        "label": "arXiv Citations",
        "message": str(total_citations),
        "color": "blue"
    }
    
    # 写入 arxiv_citations.json
    with open("arxiv_citations.json", "w") as f:
        json.dump(badge_data, f)
    
    print(f"Total citations for {len(arxiv_ids)} arXiv paper(s): {total_citations}")

if __name__ == "__main__":
    main()
