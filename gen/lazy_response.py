import time
from tornado import web, httpserver, ioloop
from tornado.options import define, options

define("port", default=8887, help="run on the given port", type=int)
from tornado import gen
from tornado.httpclient import AsyncHTTPClient


class LazyHandler(web.RequestHandler):

    def get(self):
        # Make this api block see if fast api also block too ~~
        time.sleep(14)
        self.write("Hey I lazy api ~~")

class FastHandler(web.RequestHandler):

    def get(self):
        self.write("Hey I fast api ~~")



def main():
    options.parse_command_line()
    application = web.Application([
        (r"/lz", LazyHandler),
        (r"/fs", FastHandler),
    ])
    http_server = httpserver.HTTPServer(application)
    http_server.listen(options.port)
    ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()


