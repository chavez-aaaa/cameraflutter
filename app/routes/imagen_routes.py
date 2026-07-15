from flask import Blueprint
from app.controllers.imagen_controller import recibir_imagen

imagen_bp = Blueprint("imagen", __name__)

imagen_bp.add_url_rule(
    "/imagen",
    view_func=recibir_imagen,
    methods=["POST"]
)