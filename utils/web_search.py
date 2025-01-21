from duckduckgo_search import ddg

def search_context(query):
    """Search DuckDuckGo for additional context"""
    
    try:
        results = ddg(query, max_results=3)
        context = "\n".join([result['body'] for result in results])
        return context
    except Exception as e:
        return "No additional context found." 