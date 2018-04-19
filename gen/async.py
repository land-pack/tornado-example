import mimetypes
import traceback
import base64
from uuid import uuid4
import tornado
from tornado import gen
from tornado import ioloop
from tornado import httpclient 


url_prefix = 'http://192.168.20.39:5869/upload_persist'

def get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'


def encode_multipart_formdata(fields, files):
    boundary = '----------{}'.format(uuid4())
    crlf = '\r\n'
    l = []
    for (key, value) in fields:
        l.append('--' + boundary)
        l.append('Content-Disposition: form-data; name="%s"' % key)
        l.append('')
        l.append(value)
    for (key, filename, value) in files:
        filename = filename.encode("utf8")
        l.append('--' + boundary)
        l.append(
                'Content-Disposition: form-data; name="%s"; filename="%s"' % (
                    key, filename
                )
        )
        l.append('Content-Type: %s' % get_content_type(filename))
        l.append('')
        l.append(value)
    l.append('--' + boundary + '--')
    l.append('')
    body = crlf.join(l)
    content_type = 'multipart/form-data; boundary=%s' % boundary
    return content_type, body


def base2bin(s):
    if base64.b64encode(base64.b64decode(s)) == s:
        return s.decode('base64')
    else:
        return s




@gen.coroutine
def do_upload(img):
    with open(img, 'rb') as f:



        # if you put base 64 in , will covert to binary 
        bin_data = base2bin(f.read())
        files = [('image', img, bin_data)]
        fields = []
        content_type, body = encode_multipart_formdata(fields, files)
        headers = {"Content-Type": content_type, 'content-length': str(len(body))}
        request = tornado.httpclient.HTTPRequest(url_prefix,
                                         method="POST", headers=headers, body=body, validate_cert=False)
        response = yield httpclient.AsyncHTTPClient().fetch(request)
        gen.Return(response.body)




if __name__ == '__main__':
    ioloop.IOLoop.current().run_sync(lambda: do_upload('logo.png'))
    #with open('logo.png','rb') as f:
    #    d = f.read()
        #s = covert(d)
        #print(s)
        #print('-' * 100)
        #b = base64.b64encode(d)
        #s = covert(b)
        #print(s)
        #print(base2bin(d))
