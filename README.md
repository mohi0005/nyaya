
# NyayaAI ⚖️

**AI-Assisted Legal Information & Access Platform**

## Chosen Vertical
AI for Legal Assistance & Access — helping users get quick, understandable answers to legal questions without needing to navigate complex legal jargon or hire immediate professional help.

## Approach and Logic
NyayaAI uses a FastAPI backend integrated with Google's Gemini API to process natural language legal queries and generate clear, context-aware responses. The system is designed to lower the barrier to accessing basic legal information for everyday users.

## How the Solution Works
1. User submits a legal question through the API
2. The backend validates and processes the input using Pydantic models
3. The query is sent to Gemini API with prompt engineering tailored for legal context
4. The AI-generated response is returned in a structured, readable format
5. Built-in security controls (CORS, input validation, environment-based secrets) protect the API

## Tech Stack
- **Backend:** FastAPI, Uvicorn, Gunicorn
- **AI:** Google Gemini API
- **Testing:** Pytest, Pytest-asyncio
- **Other:** Pydantic, PyPDF (document handling), Streamlit (frontend interface)

## Assumptions Made
- Users have basic internet access to reach the deployed API
- Responses are for general legal information only, not a substitute for professional legal advice
- The platform currently supports English-language queries

## Live Deployment
🔗 [https://nyaya-yuot.onrender.com](https://nyaya-yuot.onrender.com)

## API Documentation
Visit `/docs` on the deployed link for interactive API documentation (Swagger UI).

## Setup Instructions
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables (see `.env.example`)
4. Run locally: `uvicorn backend.main:app --reload`
