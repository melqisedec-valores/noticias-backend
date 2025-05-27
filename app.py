from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

NEWSAPI_KEY = os.getenv("NEWS_API_KEY")

@app.route("/noticias")
def obtener_noticias():
    url = f"https://newsapi.org/v2/top-headlines?category=business&language=es&apiKey={NEWSAPI_KEY}"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)
