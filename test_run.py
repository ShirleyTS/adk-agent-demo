from google.adk.runners import Runner
from google.adk.sessions.basic import BasicSessionService
from movie_finder_agent.agent import root_agent

runner = Runner(
    agent=root_agent,
    app_name="movie_agent_demo",
    session_service=BasicSessionService()
)

response = runner.run("Find a sci-fi movie from the 1990s")
print(response)
