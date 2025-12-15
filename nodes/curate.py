from core.state import AgentState
from langchain_google_genai import ChatGoogleGenerativeAI

def curate_node(state: AgentState):
    """
    Uses Gemini llm to read the search data and write a polished report
    """
    print("#____# I am LLM and I am analyzing data and writing report")

    llm = ChatGoogleGenerativeAI(model = "gemini-1.5-pro", temperature = 0)

    prompt = f"""
    You are a professional research assistant. 
    Topic: {state['topic']}
    
    Here is the raw data gathered from the web:
    {state['search_data']}
    
    Please write a comprehensive, polished, and professional report on this topic.
    Structure it with clear headers. Do not use markdown symbols like ** or # in the final text 
    because we are printing this to a PDF. Just use plain text with clear spacing.
    """

    response = llm.invoke(prompt)
    return {"final report": response.content}