# 🎬 ADK Movie Agent Demo

This is a demo project built with Google's **Agent Development Kit (ADK)**. The agent helps users find movies based on genre and decade, showcasing prompt-tool interactions using the `google-adk` library and Gemini models.

---

## 📦 Project Structure

adk-agent-demo/
├── movie_finder_agent/
│ ├── init.py
│ └── agent.py
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt

---

## 🚀 How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/ShirleyTS/adk-agent-demo.git
cd adk-agent-demo
```

### 2. Set up a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # on Mac/Linux
```

### 3. Install dependencies
```bash
pip install google-adk google-genai
```

### 4. Set up your API key
- Go to: https://makersuite.google.com/app/apikey
- Generate a key
- Create a .env file in the root directory:
```bash
GOOGLE_API_KEY="your-api-key-here"
```
🛡️ Never commit .env — it's ignored by .gitignore.

### 5. Run the agent
To launch the local ADK interface:
```bash
pip install google-adk google-genai
```
Or, to run from code:
```bash
python movie_finder_agent/agent.py
```
🛠 Example Prompt
"Find me a sci-fi movie from the 1990s."
The agent will invoke the find_movies() tool and return matching titles.

📚 Learn More
- Google ADK GitHub
- Gemini API Studio

🧑‍💻 Author
Created by Shirley Tauber-Sharon as an experiment with Google's ADK and agent tooling (www.linkedin.com/in/shirleytaubersharon).
Based on tutorial by George (https://medium.com/@george_6906/prompt-engineering-with-googles-agent-development-kit-adk-d748ba212440)
