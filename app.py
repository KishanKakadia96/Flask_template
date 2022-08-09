from flask import Flask, render_template, request, jsonify
from flask import Response
import os

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    try:
        return render_template("index.html")
    except Exception as e:
        return Response("this is error", e)

if __name__ == '__main__':
    app.run(debug=True)
