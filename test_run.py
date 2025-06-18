from google.adk.runners import Runner
from movie_finder_agent.agent import root_agent

runner = Runner(agent=root_agent)
response = runner.run("Find a sci-fi movie from the 1990s")
print(response)
