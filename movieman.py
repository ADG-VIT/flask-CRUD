import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(
    os.path.join(project_dir, "bookdatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


class Movie(db.Model):
    title = db.Column(db.String(80), unique=True,
                      nullable=False, primary_key=True)

    def __repr__(self):
        return "<Title: {}>".format(self.title)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        print(request.form)
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
