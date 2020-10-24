import os
from flask import Flask, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

if __name__ == "__main__":
    from models.irasas import Irasas

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'biudzetas.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

db.create_all()

@app.route("/prideti", methods=['GET', 'POST'])
def prideti():
    if request.method == "POST":
        suma = request.form['suma']
        info = request.form['info']
        irasas = Irasas(suma, info)
        db.session.add(irasas)
        db.session.commit()
        return sarasas()
    elif request.method == "GET":
        return render_template("prideti.html")

@app.route("/")
def sarasas():
        biudzetas = Irasas.query.all()
        print(biudzetas)
        return render_template("sarasas.html", biudzetas=biudzetas)

@app.route("/balansas")
def balansas():
        biudzetas = Irasas.query.all()
        balansas = 0
        for irasas in biudzetas:
            balansas += irasas.suma
        print(biudzetas)
        return render_template("balansas.html", balansas=balansas)

if __name__ == "__main__":
    app.run(debug=True)