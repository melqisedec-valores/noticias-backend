from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# Ruta principal para probar que el servidor funciona
@app.route("/")
def home():
    return "✅ API de noticias funcionando correctamente"

# Ruta para obtener noticias desde NewsAPI
@app.route("/noticias")
def obtener_noticias():
    NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWSAPI_KEY}"
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == "__main__":
    print("✅ ¡El archivo app.py se está ejecutando!")
    print("🚀 Servidor Flask escuchando en http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
