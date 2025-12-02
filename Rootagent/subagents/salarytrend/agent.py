from google.adk.agents.llm_agent import Agent
from google.adk.tools import AgentTool, FunctionTool, google_search

salary_agent = Agent(
    name="salary_agent",
    tools=[google_search],
    model="gemini-2.5-flash",
    instruction="Use search to get salary for selected roles."
)
