import falcon
from films import FilmItem
from wsgiref import simple_server

app = falcon.API()

app.add_route('/films/title/{id}', FilmItem())

if __name__ == '__main__':

    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
