# 📄 AI Resume Parser & Job Matcher

An intelligent resume parsing and job matching system powered by Groq's LLM API. This tool automatically extracts structured information from resumes, compares them against job descriptions, and ranks candidates based on match percentage.

## 🚀 Features

- **Job Description Parsing**: Extracts structured information from job descriptions (role, skills, experience, education, responsibilities)
- **Resume Parsing**: Extracts candidate information from PDF/DOCX resumes using LLM
- **Smart Matching**: Compares resumes against job descriptions and generates match scores
- **Batch Processing**: Processes multiple resumes in a folder
- **Ranking**: Automatically ranks candidates from best to worst match
- **Structured Output**: Uses Pydantic models for type-safe data extraction

## 📋 Prerequisites

- Python 3.8+
- Groq API Key

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone <repository-url>
cd week1/day5

2. Create a virtual environment (recommended)
bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Mac/Linux
source .venv/bin/activate


3. Install dependencies
bash
pip install -r requirements.txt


4. Set up environment variables
Create a .env file in the project root:

env
GROQ_API_KEY=your_groq_api_key_here


5. Add resume files
Create a resumes folder and add your resume files (PDF or DOCX):

text
resumes/
├── candidate1.pdf
├── candidate2.docx
└── candidate3.pdf


day5/
├── resume_parser.py      # Main application
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (API keys)
├── resumes/              # Folder containing resume files
│   ├── candidate1.pdf
│   └── candidate2.docx
└── README.md            # This file
