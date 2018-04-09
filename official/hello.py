import tornado.ioloop
import tornado.web
from tornado.httpclient import HTTPClient
from tornado.httpclient import AsyncHTTPClient
from tornado.concurrent import Future
from tornado import gen




class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("<h1>Hello, World!</h1>")



def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
     ])


# Here is a sample synchronous function:
def synchronous_fetch(url):

    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response.body


# And here is the same function rewritten to be asynchronous with a callback argument.
def asynchronous_fetch(url, callback):

    http_client = AsyncHTTPClient()
    def handle_response(response):
        callback(response.body)
    http_client.fetch(url, callback=handle_response)



def async_fetch_future(url):
    http_client = AsyncHTTPClient()
    my_future = http_client.fetch(url)
    fetch_future.add_done_callback(
        lambda f: my_future.set_result(f.result()))
    return my_future


@gen.coroutine
def fetch_coroutine(url):
    http_client = AsyncHTTP()
    response = yield http_client.fetch(url)
    raise gen.Return(response.body)



if __name__ == '__main__':

    app = make_app()
    app.listen(9990)
    tornado.ioloop.IOLoop.current().start()
