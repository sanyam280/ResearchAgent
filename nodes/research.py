from langchain_community.tools.tavily_search import TavilySearchResults
from core.state import AgentState

def research_node(state: AgentState):
    """
    Takes the topic, searches the web, gathers raw data.
    """

    #initalize tavily ssearch
    tool = TavilySearchResults(max_results=5)
    search_results = tool.invoke(state['topic'])


    #format results into a string
    raw_content = "\n".join([res['content'] for res in search_results])

    return {"search_data": raw_content}