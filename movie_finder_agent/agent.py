MOVIES = [
    {"title": "The Matrix", "genre": "Sci‑Fi", "year": 1999},
    {"title": "Inception", "genre": "Sci‑Fi", "year": 2010},
    # …add more entries
]

def find_movies(genre: str, decade: int) -> str:
    results = [m["title"] for m in MOVIES
               if m["genre"] == genre and decade <= m["year"] < decade+10]
    if not results:
        return "No matching movies found."
    return "\n".join(results)

from google.adk.agents import Agent

root_agent = Agent(
    name="movie_agent",
    model="gemini-2.5-flash-preview-04-17",  # or a Gemini model you have access to
    description="Answers movie‑related queries",
    instruction="You are a helpful assistant that suggests movies by genre and decade.",
    tools=[find_movies],
)

