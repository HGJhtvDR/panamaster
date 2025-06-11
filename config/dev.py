from .base import Config

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    
    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    
    # Mail
    MAIL_SUPPRESS_SEND = True  # Don't send emails in development
    
    # Security
    SESSION_COOKIE_SECURE = False  # Allow HTTP in development
    
    # Logging
    LOG_LEVEL = 'DEBUG'
    
    # Development tools
    TEMPLATES_AUTO_RELOAD = True
    SEND_FILE_MAX_AGE_DEFAULT = 0 