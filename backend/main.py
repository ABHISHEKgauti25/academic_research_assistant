# backend/main.py (FastAPI Backend)

from fastapi import FastAPI, HTTPException
from .agents.search_agent import search_papers
from .agents.database_agent import store_papers, query_papers
from .agents.qa_agent import answer_question
from .agents.future_works_agent import generate_future_works
from pydantic import BaseModel
from typing import List

app = FastAPI()

class TopicRequest(BaseModel):
    topic: str

class QueryRequest(BaseModel):
    topic: str
    year_from: int
    year_to: int

class QARequest(BaseModel):
    question: str
    papers: List[str]  # List of paper IDs or titles

class FutureWorkRequest(BaseModel):
    topic: str

@app.post("/search")
def search_topic(request: TopicRequest):
    papers = search_papers(request.topic)
    store_papers(papers)
    return {"papers": papers}

@app.post("/query")
def query_topic(request: QueryRequest):
    papers = query_papers(request.topic, request.year_from, request.year_to)
    return {"papers": papers}

@app.post("/qa")
def question_answer(request: QARequest):
    answer = answer_question(request.question, request.papers)
    return {"answer": answer}

@app.post("/future_works")
def future_works(request: FutureWorkRequest):
    future_works = generate_future_works(request.topic)
    return {"future_works": future_works}
