from google.adk.agents import Agent, LlmAgent
from google.adk.agents import SequentialAgent
from google.adk.tools import AgentTool, FunctionTool, google_search
from google.adk.agents import Agent, SequentialAgent, ParallelAgent, LoopAgent
from .subagents.profileanalyze.agent import profile_analyze_agent
from .subagents.roadmap.agent import roadmap_agent
from .subagents.careerpath.agent import career_path_agent
from .subagents.classifier.agent import classifier_agent
from .subagents.discovery.agent import discovery_agent
from .subagents.jobtrends.agent import job_trends_agent
from .subagents.salarytrend.agent import salary_agent
from .subagents.markettrend.agent import market_agent
from .subagents.researchteam.agent import research_team
from .subagents.pipeline.agent import full_pipeline





root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    instruction="""
    You are career guide mentor greet the user first if user greet us and and tell them that how you can help them and wait for reply or if not then directly do as bellow
        Step 1: ALWAYS call classifier_agent.
        Step 2: Route to correct agent:

        DISCOVERY → discovery_agent  
        PROFILE → profile_analyze_agent  
        CAREER_PATH → career_path_agent  
        ROADMAP → roadmap_agent  
        JOB_TRENDS → job_trends_agent  
        SALARY → salary_agent  
        MARKET → market_agent  
        FULL_PIPELINE → full_pipeline  

        Step 3: Return clean final output.
        """,
    tools=[
            AgentTool(classifier_agent),
            AgentTool(discovery_agent),
            AgentTool(profile_analyze_agent),
            AgentTool(career_path_agent),
            AgentTool(roadmap_agent),
            AgentTool(job_trends_agent),
            AgentTool(salary_agent),
            AgentTool(market_agent),
            AgentTool(research_team),
            AgentTool(full_pipeline),
        ]
)
