from google.adk.agents import SequentialAgent


from ..discovery.agent import discovery_agent

from ..profileanalyze.agent import profile_analyze_agent
from ..roadmap.agent import roadmap_agent
from ..researchteam.agent import research_team

full_pipeline = SequentialAgent(
    name="full_pipeline",
    sub_agents=[
        discovery_agent,
        profile_analyze_agent,
        roadmap_agent,
        research_team
    ]
)
