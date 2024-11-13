# Academic Research Assistant

This project, **Academic Research Assistant**, is a Python-based application designed to streamline the process of retrieving and managing academic papers. It includes functionalities to search for recent papers, store them in a time-series database, and display them in a user-friendly Streamlit interface. It aims to aid in efficiently handling research materials, particularly for topics like text-to-SQL, EEG applications, and other specialized fields.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

The directory structure of the project is as follows:

```
academic-research-assistant/
├── app.py
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── search_agent.py
│   │   ├── database_agent.py
│   │   ├── qa_agent.py
│   │   └── future_works_agent.py
│   └── utils/
│       ├── __init__.py
│       └── paper_processing.py
├── requirements.txt
├── README.md
└── .env
```



## Features

- **Search Agent**: Fetches academic papers on specified topics (e.g., from Arxiv).
- **Database Agent**: Stores and retrieves papers in a time-series format for easy access.
- **QA Agent**: Answers questions related to the research content.
- **Future Works Agent**: Maintains a repository of potential future research directions.
- **User Interface**: Provides a Streamlit-based interface to interact with the data.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/academic-research-assistant.git
   cd academic-research-assistant
