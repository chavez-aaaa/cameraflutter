from flask import Blueprint
from app.controllers.imagen_controller import recibir_imagen, obtener_imagen

imagen_bp = Blueprint("imagen", __name__)

imagen_bp.add_url_rule(
    "/imagen",
    view_func=recibir_imagen,
    methods=["POST"]
)
# Nueva ruta para ver/descargar la imagen (GET)
# <nombre_imagen> actuará como variable dinámica en la URL
imagen_bp.add_url_rule(
    "/imagen/<string:nombre_imagen>",
    view_func=obtener_imagen,
    methods=["GET"]
)