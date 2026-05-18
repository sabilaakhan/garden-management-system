from flask import Flask, redirect, url_for, session
from config import Config
from extensions import db
from models import User, Garden, Plant, GrowthLog, Reminder

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    # Import routes
    from routes.auth import auth_bp
    from routes.dashboard import dashboard_bp
    from routes.gardens import gardens_bp
    from routes.plants import plants_bp
    from routes.growth import growth_bp
    from routes.reminders import reminders_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(gardens_bp)
    app.register_blueprint(plants_bp)
    app.register_blueprint(growth_bp)
    app.register_blueprint(reminders_bp)
    
    @app.route('/')
    def index():
        if 'user_id' in session:
            return redirect(url_for('dashboard.index'))
        return redirect(url_for('auth.login'))
        
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
