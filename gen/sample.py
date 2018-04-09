
from tornado import web, httpserver, ioloop
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)
from tornado import gen
from tornado.httpclient import AsyncHTTPClient


class MainHandler(web.RequestHandler):


    @gen.coroutine
    def get(self):
        http_client = AsyncHTTPClient()
        url = "http://www.baidu.com"
        http_client = AsyncHTTPClient()
        response = yield http_client.fetch(url)
        print(response.body)
        self.write(response.body)
        self.finish()


def main():
    options.parse_command_line()
    application = web.Application([
        (r"/", MainHandler),
    ])
    http_server = httpserver.HTTPServer(application)
    http_server.listen(options.port)
    ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()


