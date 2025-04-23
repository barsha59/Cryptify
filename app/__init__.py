from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'our_secret_key'  #  this is required for flashing messages

    from .routes import main
    app.register_blueprint(main)

    return app
