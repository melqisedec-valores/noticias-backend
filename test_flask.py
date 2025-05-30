from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask está funcionando correctamente ✅"

if __name__ == "__main__":
    print("🧪 Servidor de prueba iniciando...")
    app.run(debug=True)
