from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object('config.Development')

@app.route("/")
def home():

    return render_template("home.html")

@app.route('/search', methods=['POST', 'GET'])
def search():

	return	render_template("search.html", query=request.form['query'])

if __name__ == "__main__":
    app.run()
