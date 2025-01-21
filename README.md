# Video Summarizer AI

A Streamlit application that uses Google's Gemini AI to generate summaries of uploaded videos, enhanced with web search context from DuckDuckGo.

## Features

- Upload videos or provide YouTube URLs
- Extract key frames from videos
- Generate AI-powered summaries using Google Gemini
- Enhance summaries with web search context
- Clean and intuitive user interface

## Setup

1. Clone the repository
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a .env file with your Google API key:
   ```
   GOOGLE_API_KEY=your_key_here
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Requirements

- Python 3.8+
- Streamlit
- Google Generative AI
- MoviePy
- DuckDuckGo Search
- Phidata
- Other dependencies listed in requirements.txt
 