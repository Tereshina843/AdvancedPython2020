from flask import Flask, render_template
import os

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, './')

app = Flask(__name__, template_folder=template_path)


@app.route('/')
def home_page():
    return render_template("static/pages/me.html")


@app.route('/cat')
def cat_page():
    return render_template("static/pages/cat.html")  # render_template("pages/cat.html")


if __name__ == "__main__":
    app.run()
