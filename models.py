import os
import requests

class film (object):

    def __init__(self, tmdb_id, image_path_base, poster_size):

        response = requests.get('http://api.themoviedb.org/3/movie/'+str(tmdb_id), 
                            	params={
                            		'api_key':os.environ['TMDB_API_KEY'],
                            		'append_to_response':'alternative_titles,credits,images,keywords,releases,trailers,translations,similar_movies,reviews'
                            	}).json()

        self.adult = response['adult']
        self.backdrop_path = response['backdrop_path']
        self.budget = response['budget']
        self.genres = response['genres']
        self.homepage = response['homepage']
        self.tmdb_id = response['id']
        self.original_title = response['original_title']
        self.overview = response['overview']
        self.poster_path = response['poster_path']
        self.popularity = response['popularity']
        self.production_companies = response['production_companies']
        self.production_countries = response['production_countries']
        self.release_date = response['release_date']
        self.release_year = response['release_date'].split('-')[0]
        self.revenue = response['revenue']
        self.runtime = response['runtime']
        self.spoken_languages = response['spoken_languages']
        self.status = response['status']
        self.tagline = response['tagline']
        self.title = response['title']
        self.vote_average = response['vote_average']
        self.vote_count = response['vote_count']
        self.alternative_titles = response['alternative_titles']
        self.credits = response['credits']
        self.images = response['images']
        self.keywords = response['keywords']
        self.releases = response['releases']
        self.trailers = response['trailers']
        self.translations = response['translations']
        self.similar_movies = response['similar_movies']
        self.reviews = response['reviews']

        # Process the poster
        
        if self.poster_path is None:

        	  self.poster_path = 'http://dummyimage.com/1000x1500/000000/ffffff.png&text=No+Poster+Found+:/'

        else:

            self.poster_path = image_path_base + poster_size + self.poster_path

        # Process the currency and budget
      
        if self.budget is 0:

            self.budget = "Unkown"

        else:

            self.budget = "${:,.2f}".format(self.budget)

        if self.revenue is 0:

            self.revenue = "Unkown"

        else:

            self.revenue = "${:,.2f}".format(self.revenue)

