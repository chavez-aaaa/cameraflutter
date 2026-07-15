from flask import Flask
from flask_cors import CORS

from app.routes.imagen_routes import imagen_bp


app = Flask(__name__)

CORS(app)

app.register_blueprint(imagen_bp)

@app.route("/")
def home():
    return {
        "mensaje": "API funcionando"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)