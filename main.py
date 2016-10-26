from flask import Flask
import controllers

app = Flask(__name__, template_folder = 'views')

app.register_blueprint(controllers.pref)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()
