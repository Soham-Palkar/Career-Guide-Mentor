from google.adk.agents.llm_agent import Agent

from google.adk.agents import Agent

profile_analyze_agent = Agent(
    name="profile_analyze_agent",
    model="gemini-2.5-flash-lite",
    description="Analyze user profile and generates strength,weakness and carreer direction",
     instruction="""
You are the Profile Analyzer Agent for an AI Career Mentor System.

Your tasks:
1. Analyze:
   - Education & Marks
   - Existing skills
   - Interests
   - Personality hint
   - Past projects
3. Extract and save structured information into memory in key:value pairs.
4. Rate the profile 

    """,
    # output_key="research_findings",
)


