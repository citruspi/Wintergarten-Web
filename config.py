class Config(object):

  DEBUG = False
  IMG_BASE_URL = 'https://image.tmdb.org/t/p/'
  POSTER_SIZE = 'original'

class Development(Config):

  DEBUG = True
