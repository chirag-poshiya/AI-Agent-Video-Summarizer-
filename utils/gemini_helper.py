import google.generativeai as genai
import os

def generate_summary(text, context):
    """Generate summary using Google Gemini"""
    
    # Configure Gemini
    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
    model = genai.GenerativeModel('gemini-pro')
    
    # Create prompt
    prompt = f"""
    Please provide a comprehensive summary of the following video content.
    Include key points, main ideas, and important details.
    
    Additional context from web search:
    {context}
    
    Video content:
    {text}
    
    Please format the summary in a clear, structured way with bullet points for key takeaways.
    """
    
    # Generate response
    response = model.generate_content(prompt)
    
    return response.text 