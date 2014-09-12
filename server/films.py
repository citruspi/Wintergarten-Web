import falcon
import json
import os
import requests

class FilmItem(object):

    def on_get (self, req, resp, id):

        extra = 'credits,images,releases,similar_movies,reviews'

        r = requests.get('http://api.themoviedb.org/3/movie/'+id,
                            params={
                                'api_key': os.environ['TMDB_API_KEY'],
                                'append_to_response': extra
                            })

        if r.status_code == 200:

            film = r.json()

            resp.status = falcon.HTTP_200
            resp.body = json.dumps(film)

        elif r.status_code == 404:

            resp.status = falcon.HTTP_404
            resp.body = ''

        else:

            resp.status = falcon.HTTP_500
            resp.body = ''

class FilmSearch(object):

    def on_get (self, req, resp, query, page=1):

        r = requests.get('http://api.themoviedb.org/3/search/movie',
                            params={
                                'api_key': os.environ['TMDB_API_KEY'],
                                'query': query,
                                'page': page
                            })

        if r.status_code == 200:

            result = r.json()

            resp.status = falcon.HTTP_200
            resp.body = json.dumps(result)

        elif r.status_code == 404:

            resp.status = falcon.HTTP_404
            resp.body = ''

        else:

            resp.status = falcon.HTTP_500
            resp.body = ''
