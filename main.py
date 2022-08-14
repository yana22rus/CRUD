from getpass import getuser
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////home/{getuser()}/aaa.db'

db = SQLAlchemy(app)


class test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=True)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        r = request.form["title"]

        create_data = test(title=r)

        db.session.add(create_data)
        db.session.flush()
        db.session.commit()

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
