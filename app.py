from flask import Flask, render_template, request, jsonify
from llm_engine import GenAILLM

app = Flask(__name__, static_folder="static", template_folder="templates")
llm = GenAILLM()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").strip()
    if not user_input:
        return jsonify({"reply": "Please type something!"})
    reply = llm.query(user_input)
    return jsonify({"reply": reply})

if __name__ == "__main__":
     app.run(debug=False)
