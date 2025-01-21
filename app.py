import streamlit as st
from utils.video_processor import process_video
from utils.gemini_helper import generate_summary
from utils.web_search import search_context
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    st.set_page_config(
        page_title="Video Summarizer AI",
        page_icon="🎥",
        layout="wide"
    )

    # Custom CSS
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
        }
        .stButton>button {
            width: 100%;
            background-color: #FF4B4B;
            color: white;
        }
        .summary-box {
            color: #222;
            padding: 20px;
            border-radius: 10px;
            background-color: #f0f2f6;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.title("🎥 Video Summarizer AI By desilo")
    st.subheader("Upload a video and get an AI-powered summary")

    # File uploader
    video_file = st.file_uploader("Upload your video", type=['mp4', 'mov', 'avi'])
    
    # URL input
    video_url = st.text_input("Or enter a YouTube URL")

    if video_file or video_url:
        with st.spinner("Processing video..."):
            # Process video and extract frames
            frames, audio_text = process_video(video_file if video_file else video_url)
            
            # Get additional context from web search
            context = search_context(audio_text[:100])  # Search based on first few words
            
            # Generate summary using Gemini
            summary = generate_summary(audio_text, context)
            
            # Display results
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("📝 Summary")
                st.markdown(f'<div class="summary-box">{summary}</div>', 
                          unsafe_allow_html=True)
            
            with col2:
                st.subheader("🖼️ Key Frames")
                for frame in frames:
                    st.image(frame, use_column_width=True)

if __name__ == "__main__":
    main() 