
# Nora — Custom AI Chatbot using Flask and GitHub-hosted OpenAI API

**Nora** is a lightweight and visually appealing web-based chatbot that enables users to interact in three intelligent modes:
- Answer a Question  
- Summarize Text  
- Generate Creative Content  

The project integrates a modern front-end interface with a Flask-powered Python backend that communicates with a custom OpenAI-compatible API hosted via GitHub (GPT-4o-mini).

---

## Features
- Three AI interaction modes (Ask, Summarize, Creative)  
- Real-time response with typing effect  
- Responsive user interface with glowing visual effects  
- Clean separation of backend and frontend, suitable for deployment  
- Distinct styling for user and AI messages  

---

## AI Model and Architecture
- **Model:** openai/gpt-4o-mini (via GitHub-hosted custom endpoint)  
- **API:** OpenAI-compatible, accessed using a GitHub token  
- **Prompt Engineering:** Dynamic prompts based on selected mode  
- **Token Limit:** Up to 1000 tokens per response  
- **Temperature:** Configurable per mode (e.g., higher for creative responses)  

---

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

---

## How to Use

### Frontend
- Choose a mode from the top (Ask, Summarize, Creative)  
- Enter your input (e.g., a question or passage)  
- Press the send button or hit Enter to receive a response  

### Backend
- Detects and processes selected mode  
- Sends the user input and generated prompt to the GPT-4o-mini model  
- Receives and returns a response to be displayed in the interface  

---

##  Setup Instructions

1. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Get your API key from GitHub Marketplace**:
   - Visit [https://github.com/marketplace](https://github.com/marketplace)
   - Subscribe to **OpenAI GPT-4o mini**
   - Generate your **GitHub-issued API key**

3. **Create a `.env` file** inside the project folder and add the following line:
   ```
   GITHUB_TOKEN=your_github_api_key_here
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Open your browser and go to**:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

Start chatting with **Nora**!

---

## Limitations
- **API Key Security:** The GitHub token is required for API access  
  - Must not be exposed publicly  
  - Stored securely in a `.env` file using `python-dotenv`  
- **Model Capability:** GPT-4o-mini is optimized for speed and light usage but is less capable than larger models  
- **Rate Limits:** Dependent on API limits and hosting performance  

---

## Advantages
- Clear separation of frontend and backend code  
- Custom user interface without reliance on heavy front-end frameworks  
- Secure API token handling using environment variables  
- Easy to extend with new modes or alternate models  
- Compatible with deployment setups such as Render (backend) and GitHub Pages (frontend)  

---

## Requirements

The following packages should be listed in `requirements.txt`:

```
Flask
openai
python-dotenv
```

---

## Future Enhancements
- Implement conversation history  
- Add user authentication and login system  
- Integrate speech-to-text and text-to-speech features  
- Include a UI-based model selector  
- Streamline and document deployment process for broader accessibility  

---

## Developed By

**Hardhik**  
Email: [hardhik318@gmail.com](mailto:hardhik318@gmail.com)  
GitHub: [github.com/Hardhik-318](https://github.com/Hardhik-318)  
LinkedIn: [linkedin.com/in/hardhik-balla](https://linkedin.com/in/hardhik-balla)  
