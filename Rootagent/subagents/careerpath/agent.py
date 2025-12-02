from google.adk.agents.llm_agent import Agent

career_path_agent = Agent(
    name="career_path_agent",
    model="gemini-2.5-flash",
    instruction="Suggest 2–4 career paths based on profile."
)
