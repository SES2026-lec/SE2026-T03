from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    nakajima="中嶋追記"
    return "Hello World! I'm using Flask."+nakajima