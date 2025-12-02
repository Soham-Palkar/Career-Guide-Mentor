from google.adk.agents.llm_agent import Agent
from google.adk.tools import AgentTool, FunctionTool, google_search

market_agent = Agent(
    name="market_agent",
    tools=[google_search],
    model="gemini-2.5-flash",
    instruction="Search companies hiring for this job."
)
