print("✅ ¡El archivo app.py se está ejecutando!")

from flask import Flask, jsonify
import requests
import os
import logging

# 🔧 CREAR LA APLICACIÓN FLASK (esto es lo que te faltaba)
app = Flask(__name__)

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/noticias")
def obtener_noticias():
    logger.info("📥 Solicitud recibida en /noticias")

    NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
    if not NEWSAPI_KEY:
        logger.error("❌ NEWSAPI_KEY no está definida")
        return jsonify({"error": "Falta la variable de entorno NEWSAPI_KEY"}), 500

    url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&language=es&apiKey={NEWSAPI_KEY}"

    try:
        response = requests.get(url)

        try:
            data = response.json()
        except ValueError:
            logger.error("❌ Error: La respuesta no es JSON válida")
            return jsonify({
                "error": "Respuesta de NewsAPI no es JSON",
                "detalle": response.text
            }), 500

        if response.status_code != 200:
            logger.error(f"❌ Error de NewsAPI: {response.status_code} - {response.text}")
            return jsonify({
                "error": "Fallo al obtener noticias",
                "status": response.status_code,
                "message": data
            }), response.status_code

        logger.info("✅ Noticias obtenidas correctamente")
        return jsonify(data)

    except Exception as e:
        logger.exception("❌ Excepción inesperada")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 Servidor Flask escuchando en http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=True)
