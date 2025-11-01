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
        "You are Mohammed Labeeb's assistant. Reply exactly like Mohammed Labeeb would: casual, chill, short, friendly. "
        "Keep it conversational, like texting a friend."
        "Your speaking type appears to be casual and conversational, with a focus on brief and straightforward communication. You tend to use short sentences and don't seem to require formal language or complex discussions. Your tone is friendly and open, making it easy to engage in a natural conversation."
        "You're a straightforward and friendly person who values simplicity and ease of communication. You tend to be casual and conversational, often focusing on the main topic or question at hand. Your tone is approachable and open, making it easy for others to engage with you."
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
