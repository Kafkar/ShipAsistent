from .root_routes import bp as root_bp
from .time_routes import bp as time_bp
from .position_routes import bp as position_bp
from .log_routes import bp as log_bp

def register_blueprints(app):
    app.register_blueprint(root_bp)
    app.register_blueprint(time_bp)
    app.register_blueprint(position_bp)
    app.register_blueprint(log_bp)
    