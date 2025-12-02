from google.adk.agents.llm_agent import Agent

from google.adk.agents import Agent

roadmap_agent = Agent(
    name="roadmap_agent",
    model="gemini-2.5-flash-lite",
    description="Generate a 30-day learning roadmap with weekly milestones and 2 mini-project ideas.",
    instruction="""
Input: 
  analyze weaknesses and strength of you will receive the analyzed profile from the previous agent, analyze weaknesses and strength and give roadmap to strengthen them
Output format:

  30_day_plan: 
    Weekly
  ,
  recomend 2 mini_projects,
  recommended_free_courses: 

""",
# output_key="research",
)

