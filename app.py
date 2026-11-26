from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    nakajima="中嶋追記"
    gui="GUIで追記"
    return "Hello World! I'm using Flask."+nakajima+gui

def ichikawa():
    ichikawa = "市川課題4"
    return "Niceな市川" +ichikawa

def kimura():
    kimura = "木村課題4"
    return "dk木村" +kimura

def master():
    master = "髙橋"
    return "end" + master