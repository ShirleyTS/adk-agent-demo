# 🎬 ADK Movie Agent Demo

This is a demo project built with Google's **Agent Development Kit (ADK)**. The agent helps users find movies based on genre and decade, showcasing prompt-tool interactions using the `google-adk` library and Gemini models.

---

## 📦 Project Structure

<pre> adk-agent-demo/
├── movie_finder_agent/
│ ├── init.py
│ └── agent.py
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
└── test_run.py </pre>

Files content:

- .env -> API keys
- movie_finder_agent/agent.py -> Tools, Agent definitions, Runner script
- movie_finder_agent/__init__.py -> Imports agent module
- README.md -> Instructions & usage
- requirements.txt -> List of dependencies
- text_run.py -> Testing file without UI
  
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
- Create a LOCAL .env file and save in it your API key as follows:
```bash
GOOGLE_API_KEY="your-api-key-here"
```
🛡️ Never commit .env file with your API key!

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
- Google ADK GitHub: https://github.com/google/adk-python
- Gemini API Studio: https://makersuite.google.com/

---

## 🧑‍💻 Author
Created by Shirley Tauber-Sharon as an experiment with Google's ADK and agent tooling (www.linkedin.com/in/shirleytaubersharon).
Based on tutorial by George (https://medium.com/@george_6906/prompt-engineering-with-googles-agent-development-kit-adk-d748ba212440)
