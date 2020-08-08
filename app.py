from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    title = "Nestor's Website"
    family_members = ["Richard", "Fiona", "Andrew", "Nestor", "Mama"]
    return render_template("home.html", title=title, family_members=family_members)


if __name__ == '__main__':
    app.run(debug=True)
