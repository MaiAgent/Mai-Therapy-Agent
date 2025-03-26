from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__, static_folder="static", template_folder="templates")

# OpenAI API Key
OPENAI_API_KEY = ""
openai.api_key = OPENAI_API_KEY

# Language translations
TRANSLATIONS = {
    "en": {
        "title": "Mai Therapy Agent - Trading Therapy",
        "welcome": "Welcome to Mai Therapy Agent! I'm here to guide your meme coin trades and provide therapy advice.",
        "placeholder": "Type your message..."
    },
    "zh": {
        "title": "Mai疗法智能体 - 交易疗法",
        "welcome": "欢迎使用Mai疗法智能体！我将指导你的迷因币交易并提供心理疗法建议。",
        "placeholder": "输入你的消息..."
    }
}

@app.route("/")
def index():
    return render_template("index.html", lang="en", translations=TRANSLATIONS["en"])

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    lang = request.json.get("lang", "en")
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are Mai Therapy Agent, a trading therapy AI. Provide guidance on meme coin trades and general therapy advice in {'Chinese' if lang == 'zh' else 'English'}."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150
        )
        ai_response = response.choices[0].message["content"]
        return jsonify({"response": ai_response})
    except Exception as e:
        return jsonify({"response": f"Error connecting to AI: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
