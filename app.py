from flask import Flask, render_template, request
from flaskext.mysql import MySQL
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Nes&and989367'
app.config['MYSQL_DATABASE_DB'] = 'fokchihin'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
app.config['MYSQL_DATABASE_PORT'] = 3306

mysql = MySQL()
mysql.init_app(app)
connection = mysql.connect()


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
    global connection
    cursor = connection.cursor()
    cursor.execute("delete from travel WHERE name = %s", name)
    connection.commit()
    cursor.close()


def add_link(name, url):
    global connection
    cursor = connection.cursor()
    cursor.execute("insert into travel(name, url) values(%s, %s)", (name, url))
    connection.commit()
    cursor.close()


def retrieve_all_links():
    global connection
    cursor = connection.cursor()
    cursor.execute("select name, url from travel")
    links = cursor.fetchall()
    cursor.close()
    return links

if __name__ == '__main__':
    app.run(debug=True, port=8080)
