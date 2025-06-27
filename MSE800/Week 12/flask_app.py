from flask import Flask

app = Flask('Vision Acuity Web')


@app.route("/")
def hello_flask():
    return "<div><h1>Kia Ora</h1></div>"