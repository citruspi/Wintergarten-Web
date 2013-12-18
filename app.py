from flask import Flask, render_template, request
import requests
import os
from models import film

app = Flask(__name__)
app.config.from_object('config.Development')

@app.route("/")
def home():

    return render_template("home.html")

@app.route('/popular', methods=['GET'])
def popular():

	response = requests.get('http://api.themoviedb.org/3/movie/popular', params={'api_key':os.environ['TMDB_API_KEY']}).json()

	films = []

	for result in response['results']:

		films.append(film(result['id'], app.config['IMG_BASE_URL']))

	return	render_template("listing.html", films=films)

@app.route('/theatres', methods=['GET'])
def theatres():

	response = requests.get('http://api.themoviedb.org/3/movie/now_playing', params={'api_key':os.environ['TMDB_API_KEY']}).json()

	films = []

	for result in response['results']:

		further = requests.get('http://api.themoviedb.org/3/movie/'+str(result['id']), params={'api_key':os.environ['TMDB_API_KEY']}).json()

		films.append(film(result['id'], app.config['IMG_BASE_URL']))		

	return	render_template("listing.html", films=films)	

@app.route('/upcoming', methods=['GET'])
def upcoming():

	response = requests.get('http://api.themoviedb.org/3/movie/upcoming', params={'api_key':os.environ['TMDB_API_KEY']}).json()

	films = []

	for result in response['results']:

		films.append(film(result['id'], app.config['IMG_BASE_URL']))

	return	render_template("listing.html", films=films)		

@app.route('/search', methods=['POST', 'GET'])
def search():

	response = requests.get('http://api.themoviedb.org/3/search/movie', params={'api_key':os.environ['TMDB_API_KEY'], 'query':request.form['query']}).json()

	films = []

	for result in response['results']:

		films.append(film(result['id'], app.config['IMG_BASE_URL']))

	return	render_template("search.html", query=request.form['query'], films=films)

if __name__ == "__main__":

	app.run()
