from flask import Flask, render_template
from joke import joke
from waitress import serve

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/joke") 
def get_joke():
    djoke = joke()
    return render_template(
        "joke.html",
        ddjoke=f"{djoke['setup']} - {djoke['punchline']}"
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
