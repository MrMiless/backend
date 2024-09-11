from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes import code_processor
    app.register_blueprint(code_processor)

    return app