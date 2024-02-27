from flask import Flask
from flask_pymongo import PyMongo
from flask_uploads import UploadSet, configure_uploads, IMAGES
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

app = Flask(__name__)

# Configuración de Mogo
app.config["MONGO_URI"] = "mongodb://localhost:27017/monas_chinas"
mongo = PyMongo(app)

photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'imagenes'
configure_uploads(app, photos)

from app import routes

