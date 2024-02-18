from flask import Flask
from src.Admin.Infraestructura.Route.MateriaRoute import materia_blueprint
from src.Admin.Infraestructura.Route.TemaRoute import tema_blueprint


app = Flask(__name__)

app.register_blueprint(materia_blueprint, url_prefix="/materia")
app.register_blueprint(tema_blueprint, url_prefix="/tema")

if __name__ == "__main__":
    app.run(debug=True)
