import os 
from dotenv import load_dotenv
from openai import OpenAI
from flask import Flask, render_template, request, jsonify

load_dotenv()

token = os.getenv("GITHUB_TOKEN")
endpoint = "https://models.github.ai/inference"
model_name = "openai/gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    print("Received data:", data)  

    message = data.get("message", "").strip()
    mode = data.get("mode", "ask")

    if not message:
        return jsonify({"reply": "No message received."}), 400

    mode_prompts = {
    "ask": (
        "You are a friendly helpful assistant. Answer the user's question clearly, "
        "factually, and concisely. Avoid adding extra explanation unless asked."
    ),
    "summarize": (
        "You are a professional summarizer. Extract the key points from the input text "
        "and present them as bullet points or a brief summary."
    ),
    "creative": (
        "You are a creative writer. Generate a short, imaginative response like a story, poem, "
        "or fictional idea based on the user's input."
    )
}



    system_prompt = mode_prompts.get(mode, "You are a helpful assistant.")

    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ],
            temperature=1.0 if mode != "ask" else 0.5,  
            top_p=1.0,
            max_tokens=1000,
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})
    except Exception as e:
        print("Error:", str(e)) 
        return jsonify({"reply": f"Error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
