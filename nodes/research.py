from langchain_tavily import TavilySearch
from core.state import AgentState

def research_node(state: AgentState):
    """
    Takes the topic, searches the web, gathers raw data.
    """

    #initalize tavily ssearch
    tool = TavilySearch(max_results=5)
    search_results = tool.invoke(state['topic'])

    print(search_results['results'])
    print(type(search_results))
    #format results into a string
    raw_content = "\n".join([res['content'] for res in search_results['results']])

    return {"search_data": raw_content}