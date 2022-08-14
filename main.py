from getpass import getuser
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////home/{getuser()}/aaa.db'

db = SQLAlchemy(app)


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=True)


@app.route("/", methods=["GET", "POST"])
@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        create_data = Test(title=request.form["title"])
        db.session.add(create_data)
        db.session.flush()
        db.session.commit()
        return "Успешно создано!"

    return render_template("index.html")


@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    if request.method == "POST":
        my_data = Test.query.get(id)
        db.session.delete(my_data)
        db.session.commit()
        return "Успешно удалено!"
    return render_template("index.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    if request.method == "POST":
        Test.query.filter_by(id=id).update({Test.title: request.form["title"]})
        db.session.flush()
        db.session.commit()
        return "Успешно изменено"

    return render_template("index.html",title=Test.query.filter_by(id=id).first().title)


if __name__ == "__main__":
    app.run(debug=True)
