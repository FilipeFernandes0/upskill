from flask import Flask
from blueprint import ex_blueprint


app = Flask(__name__)
app.register_blueprint(ex_blueprint)


@app.route('/')
def index():
    return "this is an example app"


app.run()