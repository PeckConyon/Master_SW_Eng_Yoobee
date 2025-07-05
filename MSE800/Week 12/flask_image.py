from flask import Flask, render_template

app = Flask('Vision Acuity Web')


@app.route("/image/<name>")
def browse_image(name):
     return f"{name}"
    # return render_template('index.html')

