from flask import Flask, render_template, request, abort
import wintergarten
from redis_cache import cache_it_json

app = Flask(__name__)
app.config.from_object('config.Development')

wintergarten.API_KEY = app.config['TMDB_API_KEY']
wintergarten.IMAGE_BASE = app.config['IMG_BASE_URL']
wintergarten.POSTER_SIZE = app.config['POSTER_SIZE']

@app.route("/")
def home():

    return render_template("home.html")

@app.route('/search', methods=['POST', 'GET'])
def search():

	return	render_template("search.html",
		                    query=request.form['query'],
		                    films=wintergarten.search(request.form['query']))

@app.route('/film/<id>', methods=['GET'])
def film_view(id):

	return render_template('film.html', film=wintergarten.get_film(id))

@app.route('/<listing>', methods=['GET'])
def listing(listing):

	map = {
		'popular': 'popular',
		'theatres': 'now_playing',
		'upcoming': 'upcoming'
	}

	if listing in map:

		return	render_template("listing.html", films=wintergarten.get_set(map[listing]))

	else:

		abort(404)

if __name__ == "__main__":

	app.run()
