from flask import Flask, request, render_template
import requests
from dotenv import load_dotenv
import os
from flask_cors import CORS

load_dotenv()
app = Flask(__name__)
CORS(app)

app.config["DEBUG"] = os.environ.get("FLASK_DEBUG")

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.form
    input_values = [
        float(data['sepal_length']),
        float(data['sepal_width']),
        float(data['petal_length']),
        float(data['petal_width'])
    ]
    payload = {"input": input_values}
    response = requests.post(
        "https://us-central1-ta8-project-id.cloudfunctions.net/ta8",
        headers={"Content-Type": "application/json"},
        json=payload
    )

    mapping = {0:"Setosa", 1:"Versicolor", 2:"Virginica"}
    result = response.json().get("prediction")
    return render_template("index.html", result=mapping[result]) # use mapping to print out the result in string

if __name__ == "__main__":
    app.run()