from flask import Flask

app = Flask("app")

@app.route("/")
def greeting():
    return f"{1+2}"