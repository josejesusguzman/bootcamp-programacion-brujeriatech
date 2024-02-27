from flask import request, jsonify
from app import app, mongo, photos 
import os
import uuid




@app.route('/upload', methods=['POST'])
def upload():
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'], name=str(uuid.uuid4()) + '.')
        return jsonify({"message": "Imagen cargada con éxito", "filename": filename})
    return jsonify({"error": "No se encontró el archivo"}), 400