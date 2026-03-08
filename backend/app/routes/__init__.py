from .auth import auth_bp
from .admin import admin_bp
from app.routes.company import company_bp
def register_routes(app):
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(admin_bp, url_prefix="/api/admin")
    app.register_blueprint(company_bp, url_prefix="/api/company")