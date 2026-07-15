from flask import request, jsonify
from app.services.imagen_service import guardar_imagen


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