import falcon
from films import FilmItem, FilmSearch, FilmSet
from wsgiref import simple_server

app = falcon.API()

app.add_route('/films/title/{id}/', FilmItem())
app.add_route('/films/search/{query}/', FilmSearch())
app.add_route('/films/search/{query}/{page}/', FilmSearch())
app.add_route('/films/set/{set}/', FilmSet())
app.add_route('/films/set/{set}/{page}/', FilmSet())

if __name__ == '__main__':

    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
