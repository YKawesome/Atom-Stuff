from flask import Flask, render_template
from threading import Thread

app = Flask('')



@app.route('/')
def main():
    return render_template("home.html")
def run():
    app.run(host="0.0.0.0", port=8080)
def keep_alive():
    server = Thread(target=run)
    server.start()
@app.route('/extra')
def home():
    return render_template("extra.html")
