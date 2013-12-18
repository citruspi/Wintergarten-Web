from flask import Flask, render_template, request
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

		further = requests.get('http://api.themoviedb.org/3/movie/'+str(result['id']), params={'api_key':os.environ['TMDB_API_KEY']}).json()

		print further

		imdb = requests.get('http://www.omdbapi.com/', params={'i':further['imdb_id']}).json()

		print imdb

		films.append(film(result['adult'],
						  result['backdrop_path'],
						  result['id'],
						  result['original_title'],
						  result['release_date'],
						  result['poster_path'],
						  result['title'],
						  imdb['Poster']))

	return	render_template("search.html", query=request.form['query'], films=films)

if __name__ == "__main__":

	app.run()
