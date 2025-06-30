from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
import requests

# Cargar variables de entorno (como la API Key del clima)
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return "🌱 GaiaMind API está corriendo correctamente"

@app.route('/recomendaciones')
def recomendaciones():
    ciudad = request.args.get('ciudad', default='Buenos Aires')
    api_key = os.getenv("WEATHER_API_KEY")

    if not api_key:
        return jsonify({"error": "Falta la clave de API"}), 500

    try:
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={ciudad}"
        res = requests.get(url).json()

        condicion = res['current']['condition']['text']
        if "sun" in condicion.lower():
            sugerencia = "¡Día ideal para ir en bici! 🌞"
        elif "rain" in condicion.lower() or "storm" in condicion.lower():
            sugerencia = "Mejor usar transporte público ☔"
        else:
            sugerencia = "Podés caminar o usar transporte verde 🚶‍♂️"

        return jsonify({
            "ciudad": ciudad,
            "clima": condicion,
            "sugerencia": sugerencia
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

