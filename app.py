from flask import Flask, render_template
app = Flask(__name__)
app.config.from_object('config.Development')

@app.route("/")
def search():

    return render_template("home.html")

if __name__ == "__main__":
    app.run()
