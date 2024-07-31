from flask import Blueprint, render_template

bp = Blueprint('log', __name__)

def register_log_routes(app):
    @app.route('/debug_log')
    def debug_log():
        return render_template('debug_log.html')