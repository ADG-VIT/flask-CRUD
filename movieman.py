from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        print(request.form)
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
