from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.adk.types import Content
from movie_finder_agent.agent import root_agent

runner = Runner(
    agent=root_agent,
    app_name="movie_agent_demo",
    session_service=InMemorySessionService()
)

events = runner.run(
    user_id="test-user",
    session_id="session-1",
    new_message=Content(text="Find a sci-fi movie from the 1990s")
)

for event in events:
    print(event)
