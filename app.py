from flask import Flask, request, jsonify
import cohere
import os

app = Flask(__name__)
co = cohere.Client(os.getenv("SZokWrVowtqdT95uLkyBJu0HppTDFjBZBolcuaWK"))

@app.route("/")
def home():
    return "AI Bot online!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")

    # ===== STYLE EXAMPLES =====
    style_examples = """
Friend: hey, what’s up?
You: not much, just chilling lol. u?
Friend: how was your day?
You: good, nothing crazy. you?
Friend: wanna hang later?
You: maybe, depends what time 😊
Friend: did you see that thing online?
You: yeah lol, kinda interesting
Friend: can you explain that to me?
You: sure, i'll keep it simple, basically...
"""
    # ===== END STYLE EXAMPLES =====

    prompt = f"""
You are Alex. Reply exactly like Alex would, casual and chill.
{style_examples}
Now reply to this new message:
User: {user_msg}
You:
"""

    response = co.generate(
        model="command-r",
        prompt=prompt,
        max_tokens=100,
        temperature=0.8
    )

    reply_text = response.generations[0].text.strip()
    return jsonify({"reply": reply_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
