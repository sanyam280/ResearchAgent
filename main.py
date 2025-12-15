import os
from core.graph import research_workflow
from dotenv import load_dotenv
from rich.console import Console

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')


app = research_workflow()
console = Console()
console.clear()
print("Hey, I am your ResearchAgent.")
topic = input("Enter topic to research for:")
inputs = {"topic": topic}

app.invoke(inputs)
