from google.adk.agents.llm_agent import Agent

classifier_agent = Agent(
    name="classifier_agent",
    model="gemini-2.5-flash",
    instruction="""
    Classify user query into ONE label:
    - DISCOVERY
    - PROFILE
    - CAREER_PATH
    - ROADMAP
    - JOB_TRENDS
    - SALARY
    - MARKET
    - FULL_PIPELINE

    Output ONLY the label.
    """
)