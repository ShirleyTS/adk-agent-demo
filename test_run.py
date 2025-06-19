from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from movie_finder_agent.agent import root_agent

runner = Runner(
    agent=root_agent,
    app_name="movie_agent_demo",
    session_service=InMemorySessionService()
)

response = runner.run("Find a sci-fi movie from the 1990s")
print(response)
