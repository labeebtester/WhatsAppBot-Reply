from flask import Flask, request, jsonify
import cohere
import os

app = Flask(__name__)
co = cohere.Client(os.getenv("COHERE_API_KEY"))

@app.route("/")
def home():
    return "AI Bot online!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")

    system_msg = (
        "You are Alex. Reply exactly like Alex would: casual, chill, short, friendly. "
        "Keep it conversational, like texting a friend."
    )

    try:
        response = co.chat(
            model="command-r-plus-08-2024",  # or whichever model name works for your account
            message=f"{system_msg}\nUser: {user_msg}",
            temperature=0.8
        )

        reply_text = response.text.strip()
        return jsonify({"reply": reply_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
