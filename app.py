from flask import Flask, render_template, g, request

app = Flask(__name__)
theme_color = "DarkSalmon"


@app.route('/', methods=["POST", "GET"])
def home_page():
    cat_name = "Kotik"
    if request.method == "POST":
        cat_name = request.form["cat_name"]
    return render_template("me.html", cat_name=cat_name)


@app.route('/cat')
def cat_page():
    return render_template("cat.html")


if __name__ == "__main__":
    app.run()
