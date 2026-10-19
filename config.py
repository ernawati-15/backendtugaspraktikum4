import os

class Config:
    """Base Configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key-stikom')
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """Development Configuration"""
    DEBUG = True
    ENV = 'development'

class ProductionConfig(Config):
    """Production Configuration"""
    DEBUG = False
    ENV = 'production'

# Mapping konfigurasi berdasarkan environment
config_by_name = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig,
    'default': DevelopmentConfig
}