from flask import Flask,render_template

from app.webhook.routes import webhook


# Creating our flask app


def create_app():
    app = Flask(__name__,template_folder='../templates',static_folder='../assets')

    # registering all the blueprints
    app.register_blueprint(webhook)        

    return app

