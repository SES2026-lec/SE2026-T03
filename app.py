from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    nakajima="中嶋追記"
    return "Hello World! I'm using Flask."+nakajima

def ichikawa():
    ichikawa = "市川課題4"
    return "Niceな市川" +ichikawa

def kimura():
    kimura = "木村課題4"
    return "dk木村" +kimura