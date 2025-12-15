import os
from core.graph import research_workflow
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')

app = research_workflow()

print("Yoo, I am your ResearchAgent.")
topic = input("Enter topic to research for:")
inputs = {"topic": topic}

app.invoke(inputs)
