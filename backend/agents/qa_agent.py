# agents/qa_agent.py
from transformers import pipeline
from typing import List
import os

# Load a language model for Q&A
qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

def answer_question(question: str, papers: List[str]):
    # For simplicity, concatenate summaries of selected papers
    context = ""
    for paper_id in papers:
        # Fetch the paper summary from the database
        summary = get_paper_summary(paper_id)
        context += summary + " "
    print(context)
    answer = qa_pipeline(question=question, context=context)
    print(answer['answer'])
    return answer['answer']

def get_paper_summary(paper_id: str):
    # Fetch paper summary from Neo4j
    from neo4j import GraphDatabase
    NEO4J_URI = os.getenv('NEO4J_URI')
    NEO4J_USERNAME = os.getenv('NEO4J_USERNAME')
    NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))
    with driver.session() as session:
        result = session.run(
            """
            MATCH (p:Paper {id: $id})
            RETURN p.summary AS summary
            """,
            id=paper_id
        )
        record = result.single()
        if record:
            print(record['summary'])
            return record['summary']
        else:
            return ""
