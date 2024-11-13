# agents/search_agent.py
from typing import List
from ..utils.paper_processing import process_paper
import arxiv

def search_papers(topic: str) -> List[dict]:
    search = arxiv.Search(
        query=topic,
        max_results=10,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    papers = []
    for result in search.results():
        paper_info = {
            "id": result.entry_id,
            "title": result.title,
            "summary": result.summary,
            "authors": [author.name for author in result.authors],
            "published": result.published,
            "pdf_url": result.pdf_url
        }
        papers.append(paper_info)
        # Optionally download and process the paper
        # process_paper(result.pdf_url, result.entry_id)
    return papers
