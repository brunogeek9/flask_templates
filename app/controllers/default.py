from app import app

@app.route("/")
def index():
    return "<h1> Bem vindo </h1>"
