# Nora — Custom AI Chatbot using Flask and GitHub-hosted OpenAI API

**🔗 Live Demo: [nora-chatbot.onrender.com](https://nora-chatbot.onrender.com)**

Nora is a lightweight, visually appealing web-based chatbot that lets users interact in three intelligent modes:

- **Answer a Question**
- **Summarize Text**
- **Generate Creative Content**

Try it live — no installation needed. The link above is a fully working deployment.

## Overview

Nora integrates a modern front-end interface with a Flask-powered Python backend that communicates with a custom OpenAI-compatible API hosted via GitHub (GPT-4o-mini).

## Features

- Three AI interaction modes (Ask, Summarize, Creative)
- Real-time response with typing effect
- Responsive UI with glowing visual effects
- Clean separation of backend and frontend, suitable for deployment
- Distinct styling for user and AI messages

## AI Model and Architecture

| | |
|---|---|
| **Model** | `openai/gpt-4o-mini` (via GitHub-hosted custom endpoint) |
| **API** | OpenAI-compatible, accessed using a GitHub token |
| **Prompt Engineering** | Dynamic prompts based on selected mode |
| **Token Limit** | Up to 1000 tokens per response |
| **Temperature** | Configurable per mode (e.g., higher for creative responses) |

## Project Structure

```
app.py               -> Flask backend
.env                 -> Contains GitHub token (GITHUB_TOKEN)
templates/
  └── index.html     -> Frontend HTML
static/
  ├── styles.css     -> Styling (CSS)
  └── script.js      -> Client-side JavaScript
requirements.txt     -> Python dependencies
```

## How to Use (Live Demo)

1. Open **[nora-chatbot.onrender.com](https://nora-chatbot.onrender.com)**
2. Choose a mode from the top (Ask, Summarize, Creative)
3. Enter your input (e.g., a question or passage)
4. Press the send button or hit Enter to receive a response

Under the hood, the backend detects the selected mode, sends the input and a mode-specific generated prompt to GPT-4o-mini, and returns the response to the interface.

## Run It Locally (optional)

Prefer to run Nora on your own machine instead of the hosted version? Here's how:

<details>
<summary>Local setup instructions</summary>

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Get your API key from [GitHub Marketplace](https://github.com/marketplace):
   - Subscribe to OpenAI GPT-4o mini
   - Generate your GitHub-issued API key
3. Create a `.env` file in the project folder:
   ```
   GITHUB_TOKEN=your_github_api_key_here
   ```
4. Run the app:
   ```
   python app.py
   ```
5. Open `http://127.0.0.1:5000` in your browser

</details>

## Limitations

- **API Key Security** — the GitHub token is required for API access, must not be exposed publicly, and is stored securely via `.env` and `python-dotenv`
- **Model Capability** — GPT-4o-mini is optimized for speed and light usage, but less capable than larger models
- **Rate Limits** — dependent on API limits and hosting performance

## Advantages

- Clear separation of frontend and backend code
- Custom UI without reliance on heavy front-end frameworks
- Secure API token handling using environment variables
- Easy to extend with new modes or alternate models
- Compatible with deployment setups such as Render (backend) and GitHub Pages (frontend)

## Requirements (`requirements.txt`)

```
Flask
openai
python-dotenv
```

## Future Enhancements

- Implement conversation history
- Add user authentication and login system
- Integrate speech-to-text and text-to-speech features
- Include a UI-based model selector
- Streamline and document deployment process for broader accessibility

## Developed By

**Hardhik**
Email: hardhik318@gmail.com..
GitHub: [github.com/Hardhik-318](https://github.com/Hardhik-318)..
LinkedIn: [linkedin.com/in/hardhik-balla](https://linkedin.com/in/hardhik-balla)
