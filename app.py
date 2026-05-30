from flask import Flask
from flask import render_template
from flask import request

from chatboat import get_bot_response

app = Flask(__name__)

chat_history = []

@app.route("/")
def home():

    return render_template(
        "index.html",
        chats=chat_history
    )


@app.route("/get")
def get_bot():

    user_msg = request.args.get("msg", "")

    bot_reply = get_bot_response(user_msg)

    chat_history.append(
        {
            "user": user_msg,
            "bot": bot_reply
        }
    )

    return render_template(
        "index.html",
        chats=chat_history
    )


if __name__ == "__main__":
    app.run(debug=True)