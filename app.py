from flask import Flask, render_template, request, abort, jsonify
import requests
import os
from pymongo import MongoClient
from wintergarten import Wintergarten

app = Flask(__name__)
app.config.from_object('config.Development')

database = MongoClient(app.config['MONGODB_HOST'],
	                   app.config['MONGODB_PORT'])['MONGODB_DATABASE']

w = Wintergarten(os.environ['TMDB_API_KEY'],
				 database,
				 app.config['IMG_BASE_URL'],
				 app.config['POSTER_SIZE'])

@app.route("/")
def home():

    return render_template("home.html")	

@app.route('/search', methods=['POST', 'GET'])
def search():

	return	render_template("search.html", 
		                    query=request.form['query'], 
		                    films=w.search(request.form['query']))

@app.route('/film/<id>', methods=['GET'])
def film_view(id):

	return render_template('film.html', film=w.get_film(id))

@app.route('/<listing>', methods=['GET'])
def listing(listing):

	map = {
		'popular': 'popular',
		'theatres': 'now_playing',
		'upcoming': 'upcoming'
	}

	if listing in map:

		return	render_template("listing.html", films=w.get_set(map[listing]))	

	else:

		abort(404)

if __name__ == "__main__":

	app.run()
