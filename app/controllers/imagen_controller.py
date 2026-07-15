from flask import request, jsonify, send_from_directory
from app.services.imagen_service import guardar_imagen
import os

def recibir_imagen():

    try:

        data = request.get_json()

        if data is None:
            return jsonify({
                "success": False,
                "message": "No se recibió JSON"
            }), 400

        image_name = data.get("imageName")
        image_base64 = data.get("imageBase64")
        sent_at = data.get("sentAt")

        if not image_name:
            return jsonify({
                "success": False,
                "message": "imageName es obligatorio"
            }), 400

        if not image_base64:
            return jsonify({
                "success": False,
                "message": "imageBase64 es obligatorio"
            }), 400

        ruta = guardar_imagen(image_name, image_base64)

        return jsonify({
            "success": True,
            "message": "Imagen recibida correctamente",
            "imageName": image_name,
            "savedPath": ruta,
            "sentAt": sent_at
        }), 200

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500
    # Define la ruta absoluta o relativa a tu carpeta de uploads
# Si está en la raíz del proyecto, puedes configurarla en el config de Flask o definirla aquí:
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')

def obtener_imagen(nombre_imagen):
    try:
        # Verificamos si el archivo realmente existe antes de enviarlo
        if not os.path.exists(os.path.join(UPLOAD_FOLDER, nombre_imagen)):
            return jsonify({
                "success": False,
                "message": f"La imagen '{nombre_imagen}' no existe."
            }), 404

        # Enviamos el archivo desde el directorio seguro
        return send_from_directory(UPLOAD_FOLDER, nombre_imagen)

    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error al recuperar la imagen: {str(e)}"
        }), 500