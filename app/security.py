from flask import request, current_app
from functools import wraps
import hashlib
import secrets
import hmac
import base64

def generate_csrf_token():
    """Генерирует безопасный CSRF токен"""
    return secrets.token_hex(32)

def hash_password(password):
    """Безопасное хеширование пароля с использованием PBKDF2"""
    salt = secrets.token_hex(16)
    iterations = 100000
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt.encode('utf-8'),
        iterations
    )
    return f"{salt}${iterations}${base64.b64encode(key).decode('utf-8')}"

def verify_password(password, hashed):
    """Проверка пароля"""
    salt, iterations, stored_key = hashed.split('$')
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt.encode('utf-8'),
        int(iterations)
    )
    return hmac.compare_digest(
        base64.b64encode(key).decode('utf-8'),
        stored_key
    )

def apply_security_headers(response):
    """Применяет заголовки безопасности к ответу"""
    # CSP
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdn.jsdelivr.net; style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://cdnjs.cloudflare.com; img-src 'self' data:; font-src 'self' https://cdnjs.cloudflare.com;"
    
    # Referrer Policy
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    
    # Permissions Policy
    response.headers['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'
    
    # Clear-Site-Data
    if request.endpoint == 'auth.logout':
        response.headers['Clear-Site-Data'] = '"cache", "cookies", "storage"'
    
    return response

def security_headers(f):
    """Декоратор для применения заголовков безопасности к маршруту"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        response = f(*args, **kwargs)
        return apply_security_headers(response)
    return decorated_function 