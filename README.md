# Restaurant & Menu Generator

An AI-powered Restaurant Name & Menu Generator built with LangChain and Google Gemini, with a Streamlit UI.  

This app helps you:
- Generate unique restaurant names based on cuisine, style, or theme  
- Create customized menus with AI, including dish names, descriptions, and categories  

## Features
- Generate creative restaurant names  
- Auto-generate menus (appetizers, mains, desserts, drinks, etc.)  
- Powered by LangChain + Google Gemini for structured LLM workflows  
- Interactive Streamlit UI for easy use  
- Flexible inputs (cuisine, target audience, theme, etc.)  

## Tech Stack
- Python 3.9+  
- LangChain  
- Google Gemini  
- Streamlit  

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Gen-AI-Restaurent-Name-Item-Generation.git
```


Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Environment Variables

Create a .env file in the project root:
```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

## Usage
Run the Streamlit app:

```bash
streamlit run app.py
```
## Project Structure
```bash
.
├── Langchain-Model-Task/LAngchain-Gemini-Model.ipynb
├── app.py              # Main Streamlit app
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment file
├── .gitignore
└── README.md
```