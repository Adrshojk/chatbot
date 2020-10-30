from flask import Flask,render_template,request,jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app=Flask(__name__)
english_bot = ChatBot("ChatterBot",storage_adapter="chatterbot.storage.SQLStorageAdapter",logic_adapters=['chatterbot.logic.BestMatch'])
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
trainer.train("data/data.yml")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    data = str(english_bot.get_response(userText))
    return jsonify(data=data),200

if __name__ == '__main__' :
    app.run(debug=True)
