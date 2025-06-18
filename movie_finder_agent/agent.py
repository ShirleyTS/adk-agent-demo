# movie_finder_agent/agent.py

from google.adk.agents import Agent

# A sample movie database
MOVIES = [
    {"title": "The Matrix", "genre": "Sci-Fi", "year": 1999},
    {"title": "Inception", "genre": "Sci-Fi", "year": 2010},
    {"title": "Pulp Fiction", "genre": "Crime", "year": 1994},
    {"title": "The Godfather", "genre": "Crime", "year": 1972},
    {"title": "The Shawshank Redemption", "genre": "Drama", "year": 1994},
    {"title": "Blade Runner", "genre": "Sci-Fi", "year": 1982},
]

# A simple tool function the agent can use
def find_movies(genre: str, decade: int) -> str:
    results = [
        m["title"] for m in MOVIES
        if m["genre"].lower() == genre.lower() and decade <= m["year"] < decade + 10
    ]
    return "\n".join(results) if results else "No matching movies found."

# The agent definition
root_agent = Agent(
    name="movie_agent",
    model="gemini-2.5-flash-preview-04-17",  # use your accessible Gemini model
    description="Answers movie-related queries",
    instruction="You are a helpful assistant that suggests movies by genre and decade.",
    tools=[find_movies],
)
