import os
import requests

class Wintergarten (object):

    def __init__ (self, 
                  api_key, 
                  database, 
                  image_base='https://image.tmdb.org/t/p/', 
                  poster_size='original'):

        self.api_key = api_key
        self.database = database
        self.image_base = image_base
        self.poster_size = poster_size

    def search (self, query):

        response = requests.get('http://api.themoviedb.org/3/search/movie', params={
            'api_key': self.api_key,
            'query': query
        }).json()['results']

        results = []

        for result in response:

            results.append(self.get_film(result['id']))

        return results

    def get_film (self, tmdb_id):

        query = self.database.Films.find_one({
            "tmdb_id": int(tmdb_id)
        })

        if query:

            film = query

        else:

            film = requests.get('http://api.themoviedb.org/3/movie/'+str(tmdb_id), 
                                params={
                                    'api_key': self.api_key,
                                    'append_to_response': 'alternative_titles,credits,images,keywords,releases,trailers,translations,similar_movies,reviews'
                                }).json()
            
            film['tmdb_id'] = film.pop('id')
            film['release_year'] = film['release_date'].split('-')[0]

            if film['poster_path'] is None:

                film['poster_path'] = 'http://dummyimage.com/1000x1500/000000/ffffff.png&text=No+Poster+Found+:/'

            else:

                film['poster_path'] = self.image_base + self.poster_size + film['poster_path']

            if film['budget'] is 0:

                film['budget'] = "Unknown"

            else:

                film['budget'] = "${:,.2f}".format(film['budget'])

            if film['revenue'] is 0:

                film['revenue'] = "Unknown"

            else:

                film['revenue'] = "${:,.2f}".format(film['revenue'])

            self.database.Films.insert(film)                

        return film

    def get_set (self, set):

        r = []

        query = self.database.Sets.find_one({
            'set_id': set
        })

        if query:

            r = query['set']

        else:

            response = requests.get('http://api.themoviedb.org/3/movie/' + set, params={
                'api_key': self.api_key
            }).json()['results']

            for result in response:

                r.append(self.get_film(result['id']))

            self.database.Sets.insert({
                'set_id': set,
                'set': r
            })

        return r
