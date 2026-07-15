import os
import base64


UPLOAD_FOLDER = "uploads"


def guardar_imagen(nombre, imagen_base64):

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    if "," in imagen_base64:
        imagen_base64 = imagen_base64.split(",")[1]

    datos = base64.b64decode(imagen_base64)

    ruta = os.path.join(UPLOAD_FOLDER, nombre)

    with open(ruta, "wb") as archivo:
        archivo.write(datos)

    return ruta