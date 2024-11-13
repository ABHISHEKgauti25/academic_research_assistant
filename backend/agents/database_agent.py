# agents/database_agent.py
from neo4j import GraphDatabase
from typing import List
import os

NEO4J_URI = os.getenv('NEO4J_URI')
NEO4J_USERNAME = os.getenv('NEO4J_USERNAME')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

def store_papers(papers: List[dict]):
    with driver.session() as session:
        for paper in papers:
            session.run(
                """
                MERGE (p:Paper {id: $id})
                SET p.title = $title,
                    p.summary = $summary,
                    p.published = date($published),
                    p.pdf_url = $pdf_url
                """,
                id=paper['id'],
                title=paper['title'],
                summary=paper['summary'],
                published=paper['published'].strftime('%Y-%m-%d'),
                pdf_url=paper['pdf_url']
            )

def query_papers(topic: str, year_from: int, year_to: int):
    with driver.session() as session:
        result = session.run(
            """
            MATCH (p:Paper)
            WHERE p.title CONTAINS $topic AND p.published >= date($year_from + '-01-01') AND p.published <= date($year_to + '-12-31')
            RETURN p
            """,
            topic=topic,
            year_from=str(year_from),
            year_to=str(year_to)
        )
        papers = []
        for record in result:
            p = record['p']
            papers.append({
                'id': p['id'],
                'title': p['title'],
                'summary': p['summary'],
                'published': p['published'],
                'pdf_url': p['pdf_url']
            })
        return papers
