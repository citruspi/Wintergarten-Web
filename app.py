from flask import Flask, render_template, request, abort
import requests
import os
from models import film

app = Flask(__name__)
app.config.from_object('config.Development')

@app.route("/")
def home():

    return render_template("home.html")	

@app.route('/search', methods=['POST', 'GET'])
def search():

	response = requests.get('http://api.themoviedb.org/3/search/movie', params={'api_key':os.environ['TMDB_API_KEY'], 'query':request.form['query']}).json()

	films = []

	for result in response['results']:

		films.append(film(result['id'], app.config['IMG_BASE_URL']))

	return	render_template("search.html", query=request.form['query'], films=films)

@app.route('/film/<id>', methods=['GET'])
def film_view(id):

	f = film(id, app.config['IMG_BASE_URL'])

	return render_template('film.html', film=f)

@app.route('/<listing>', methods=['GET'])
def listing(listing):

	map = {

		'popular': 'popular',
		'theatres': 'now_playing',
		'upcoming': 'upcoming'

	}

	if listing in map:

		response = requests.get('http://api.themoviedb.org/3/movie/' + map[listing], params={'api_key':os.environ['TMDB_API_KEY']}).json()

		films = []

		for result in response['results']:

			films.append(film(result['id'], app.config['IMG_BASE_URL']))

		return	render_template("listing.html", films=films)	

	else:

		abort(404)

if __name__ == "__main__":

	app.run()
