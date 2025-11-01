from flask import Flask, request, jsonify
import cohere
import os

app = Flask(__name__)

# Safe API key usage
co = cohere.Client(os.getenv("COHERE_API_KEY"))

@app.route("/")
def home():
    return "AI Bot online!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")

    # System message defines your style
    system_msg = (
        "You are Alex. Reply exactly like Alex would, casual, chill, short, and friendly. "
        "Keep it conversational and simple, like texting a friend."
    )

    # Call Cohere Chat API
    try:
        response = co.chat(
            model="xlarge",
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_msg}
            ],
            temperature=0.8
        )

        # Get the generated reply
        reply_text = response.output[0].content.strip()
        return jsonify({"reply": reply_text})

    except Exception as e:
        # Catch errors to avoid crashing the server
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # For Render, host on 0.0.0.0 and port 10000
    app.run(host="0.0.0.0", port=10000)
