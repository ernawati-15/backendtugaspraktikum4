from flask import Flask
from app.config import config_by_name
from app.routes.umkm_routes import umkm_bp

def create_app(config_name='dev'):
    app = Flask(__name__)
    
    # Memuat Konfigurasi dari config.py
    app.config.from_object(config_by_name[config_name])
    
    # Registrasi Blueprint
    app.register_blueprint(umkm_bp)
    
    return app