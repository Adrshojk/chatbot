import aiml
from flask import Flask,request,jsonify
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

@app.route("/")
def index():
    return "server is up"


@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    data = kernel.respond(userText)
    return jsonify(data=data),200

if __name__ == '__main__' :
    app.run(debug=True)

