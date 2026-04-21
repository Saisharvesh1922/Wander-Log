from flask import Flask, request, jsonify
from chatbot import create_user_chatbot
from dotenv import load_dotenv
from flask_cors import CORS
import traceback

from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json

    user_stories = data.get("userStories", [])
    question = data.get("question", "")
    chat_history = data.get("chatHistory", [])

    print("Incoming question:", question)
    print("Stories count:", len(user_stories))

    if not user_stories or not question:
        return jsonify({"error": "Missing data"}), 400

    try:
        chatbot = create_user_chatbot(user_stories)

        
        converted_history = []
        for msg in chat_history:
            if msg.get("type") == "human":
                converted_history.append(HumanMessage(content=msg["content"]))
            elif msg.get("type") == "ai":
                converted_history.append(AIMessage(content=msg["content"]))

        
        result = chatbot.invoke({
            "question": question,
            "chat_history": converted_history
        })

        print("FULL RESULT:", result)

        answer = result.get("answer") or result.get("result") or "No answer received"

        return jsonify({
            "answer": answer
        })

    except Exception as e:
        print("🔥 ERROR START 🔥")
        traceback.print_exc()
        print("🔥 ERROR END 🔥")

        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, port=2000)