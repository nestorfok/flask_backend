from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    title = "Nestor's Website"
    family_members = ["Richard", "Fiona", "Andrew", "Nestor", "Mama"]
    links = {
        "Hong Kong": "https://www.google.com/travel/things-to-do?dest_mid=%2Fm%2F07dfk&dest_state_type=main&dest_src=yts&g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4308227%2C4317915%2C4322823%2C4328159%2C4367953%2C4371335%2C4393965%2C4395848%2C4401769%2C4403882%2C4412670%2C4413451%2C4416581%2C4417925%2C4421968&hl=en&gl=GB#ttdm=35.612241_139.789860_10&ttdmf=%25252Fm%25252F07thkr",
        "Tokyo": "https://www.google.com/maps/d/viewer?ie=UTF8&hl=en&msa=0&ll=22.296243999999998%2C114.173183&spn=0.052095%2C0.110378&z=14&iwloc=000488f2abc26e2aa5aa0&mid=1FA5MzT9LlPsr6YRXMEU9cYv9TzM"
    }
    return render_template("home.html", title=title, family_members=family_members, links=links)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
