import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("Academic Research Paper Assistant")

st.sidebar.title("Find Here")

topic = st.sidebar.text_input("Enter Research Topic", value="Text-to-SQL")

if st.sidebar.button("Search Papers"):
    # Call the backend API to search and store papers
    response = requests.post(f"{API_URL}/search", json={"topic": topic})
    papers = response.json().get("papers", [])
    if papers:
        st.session_state['papers'] = papers
        st.success(f"Found {len(papers)} papers on '{topic}'")
    else:
        st.error("No papers found.")

if 'papers' in st.session_state:
    st.header(f"Papers on {topic}")
    selected_papers = st.multiselect(
        "Select Papers for Q&A",
        options=[paper['title'] for paper in st.session_state['papers']],
        default=[]
    )
    question = st.text_input("Enter your question")
    if st.button("Ask a Question"):
        
        if question and selected_papers:
            # Get the IDs of the selected papers
            paper_ids = [paper['id'] for paper in st.session_state['papers'] if paper['title'] in selected_papers]
            response = requests.post(f"{API_URL}/qa", json={"question": question, "papers": paper_ids})
            answer = response.json().get("answer", "")
            st.write("Answer:")
            st.write(answer)
        else:
            st.error("Please enter a question and select at least one paper.")

    if st.button("Generate Future Works"):
        response = requests.post(f"{API_URL}/future_works", json={"topic": topic})
        future_works = response.json().get("future_works", "")
        st.write("Future Research Directions:")
        st.write(future_works)
