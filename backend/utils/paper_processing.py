# utils/paper_processing.py
import requests
import os

def process_paper(pdf_url: str, paper_id: str):
    response = requests.get(pdf_url)
    pdf_path = os.path.join('data', 'papers', f"{paper_id}.pdf")
    with open(pdf_path, 'wb') as f:
        f.write(response.content)
    # Additional processing can be done here (e.g., extracting text, images)
