import os
import requests
from redis_cache import cache_it_json
import json

API_KEY = None
IMAGE_BASE = 'https://image.tmdb.org/t/p/'
POSTER_SIZE = 'original'

@cache_it_json(limit=100000, expire=60 * 60 * 24)
def get_film (tmdb_id):

    film = requests.get('http://api.themoviedb.org/3/movie/'+str(tmdb_id),
                        params={
                            'api_key': API_KEY,
                            'append_to_response': 'alternative_titles,credits,images,keywords,releases,trailers,translations,similar_movies,reviews'
                        }).json()

    film['tmdb_id'] = film.pop('id')
    film['release_year'] = film['release_date'].split('-')[0]

    if film['poster_path'] is None:

        film['poster_path'] = 'http://dummyimage.com/1000x1500/000000/ffffff.png&text=No+Poster+Found+:/'

    else:

        film['poster_path'] = IMAGE_BASE + POSTER_SIZE + film['poster_path']

    if film['budget'] is 0:

        film['budget'] = "Unknown"

    else:

        film['budget'] = "${:,.2f}".format(film['budget'])

    if film['revenue'] is 0:

        film['revenue'] = "Unknown"

    else:

        film['revenue'] = "${:,.2f}".format(film['revenue'])

    return film


@cache_it_json(limit=100000, expire=60 * 60 * 24)
def search (query):

    response = requests.get('http://api.themoviedb.org/3/search/movie', params={
        'api_key': API_KEY,
        'query': query
    }).json()['results']

    results = []

    for result in response:

        results.append(get_film(result['id']))

    return results


@cache_it_json(limit=100000, expire=60 * 60 * 24)
def get_set (set):

    r = []

    response = requests.get('http://api.themoviedb.org/3/movie/' + set, params={
        'api_key': API_KEY
    }).json()['results']

    for result in response:

        r.append(get_film(result['id']))

    return r
