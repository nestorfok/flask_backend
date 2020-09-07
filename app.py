from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

### Setup SQLAlchemy connection ###
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="root",
    password="",
    hostname="127.0.0.1",
    databasename="Destinations",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# Mysql table
class Travel(db.Model):
    __tablename__ = "travel"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    url = db.Column(db.String(2083))


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        if request.form.get('name_delete'):
            name = request.form.get('name_delete')
            delete_link(name)
        elif request.form.get('name_add'):
            name = request.form.get('name_add')
            url = request.form.get('url')
            add_link(name, url)

    title = "Nestor's Website"
    family_members = ["Richard", "Fiona", "Andrew", "Nestor", "Mama"]
    links = retrieve_all_links()

    return render_template("home.html", title=title, family_members=family_members, links=links)


def delete_link(name):
    record = Travel.query.filter_by(name=name).first()
    db.session.delete(record)
    db.session.commit()
    return


def add_link(name, url):
    comment = Travel(name=name, url=url)
    db.session.add(comment)
    db.session.commit()


def retrieve_all_links():
    return Travel.query.all()

if __name__ == '__main__':
    app.run(debug=True, port=8080)
