from google.adk.agents import ParallelAgent

from ..jobtrends.agent import job_trends_agent
from ..salarytrend.agent import salary_agent
from ..markettrend.agent import market_agent

research_team = ParallelAgent(
    name="parallel_research_team",
    sub_agents=[job_trends_agent, salary_agent, market_agent]
)
