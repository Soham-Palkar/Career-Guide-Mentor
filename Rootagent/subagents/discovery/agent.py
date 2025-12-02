from google.adk.agents.llm_agent import Agent

discovery_agent = Agent(
    name="discovery_agent",
    model="gemini-2.5-flash-lite",
    instruction="""
    If user is confused about career:
    ask questions → extract interests, strengths, possible domains.
    Output JSON.
    """
)
