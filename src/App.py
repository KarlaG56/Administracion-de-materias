from flask import Flask
from src.Admin.Infraestructura.Route.MateriaRoute import materia_blueprint


app = Flask(__name__)

app.register_blueprint(materia_blueprint, url_prefix="/materia")

if __name__ == "__main__":
    app.run(debug=True)
