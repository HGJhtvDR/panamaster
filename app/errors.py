from flask import render_template, request, jsonify, current_app
from werkzeug.exceptions import HTTPException
import traceback
import logging

def init_error_handlers(app):
    @app.errorhandler(400)
    def bad_request_error(error):
        if request.is_json:
            return jsonify({
                'error': 'Bad Request',
                'message': str(error)
            }), 400
        return render_template('errors/400.html'), 400

    @app.errorhandler(401)
    def unauthorized_error(error):
        if request.is_json:
            return jsonify({
                'error': 'Unauthorized',
                'message': 'Please authenticate to access this resource'
            }), 401
        return render_template('errors/401.html'), 401

    @app.errorhandler(403)
    def forbidden_error(error):
        if request.is_json:
            return jsonify({
                'error': 'Forbidden',
                'message': 'You do not have permission to access this resource'
            }), 403
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(405)
    def method_not_allowed_error(error):
        if request.is_json:
            return jsonify({
                'error': 'Method Not Allowed',
                'message': 'The method is not allowed for the requested URL'
            }), 405
        return render_template('errors/405.html'), 405

    @app.errorhandler(429)
    def too_many_requests_error(error):
        if request.is_json:
            return jsonify({
                'error': 'Too Many Requests',
                'message': 'Rate limit exceeded'
            }), 429
        return render_template('errors/429.html'), 429

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('errors/500.html'), 500

    @app.errorhandler(Exception)
    def unhandled_exception(error):
        # Логирование необработанного исключения
        current_app.logger.error(f'Unhandled Exception: {error}')
        current_app.logger.error(traceback.format_exc())
        
        if isinstance(error, HTTPException):
            return error
        
        if request.is_json:
            return jsonify({
                'error': 'Internal Server Error',
                'message': 'An unexpected error occurred'
            }), 500
        return render_template('errors/500.html'), 500 