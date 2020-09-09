from flask import Flask, render_template, request
from PredictNote import PredictNote

app = Flask(__name__)

#MARK : route function
@app.route('/')
def home():
    return render_template("index.html")

@app.route("/PredictNote", methods=["POST", "GET"])
def predict_note():
    if request.method == "POST":
        G1 = request.form["note1"]
        G2 = request.form["note2"]
        G3 = PredictNote(G1, G2)
        return render_template("edith.html", prediction=G3)

    else:
        return render_template("edith.html")

@app.route("/edith")
def edith():
    return render_template("edith.html")

@app.route("/sites_associé")
def sites_associé():
    return render_template("sites_associé.html")

@app.route("/aide")
def aide():
    return render_template("aide.html")

@app.route("/index")
def index():
    return render_template("index.html")

#MARK : main
if __name__ == '__main__':
    app.run(debug=True)