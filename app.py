# app.py
from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

NEWSAPI_KEY = "8be3c9b58cbc48b4bef066357d743946"

@app.route("/noticias")
def obtener_noticias():
    url = f"https://newsapi.org/v2/top-headlines?category=business&language=es&apiKey={NEWSAPI_KEY}"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
