from flask import Flask, render_template

app = Flask('Vision Acuity Web')


@app.route("/")
def browse_image():
    return render_template('index.html')

