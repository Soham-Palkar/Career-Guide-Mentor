from google.adk.agents.llm_agent import Agent

from google.adk.tools import AgentTool, FunctionTool, google_search

job_trends_agent = Agent(
    name="job_trends_agent",
    tools=[google_search],
    model="gemini-2.5-flash",
    instruction="Use search tool to fetch and summarize job trends."
)
