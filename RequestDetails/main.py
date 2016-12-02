import pprint

from flask import Flask
from flask import request

app = Flask(__name__)

captured = ""


class LoggingMiddleware:

    def __init__(self, app):
        self._app = app

    def __call__(self, environ, resp):
        errorlog = environ['wsgi.errors']
        pprint.pprint(("REQUEST", environ), stream=errorlog)

        def log_response(status, headers, *args):
            global captured
            captured = (
                pprint.pformat(("REQUEST", environ), indent=4) +
                pprint.pformat(("RESPONSE", status, headers), indent=4)
            )
            pprint.pprint(("RESPONSE", status, headers), stream=errorlog)
            return resp(status, headers, *args)

        return self._app(environ, log_response)


@app.route("/")
def request_details():
    return "<pre>{captured}</pre>".format(captured=captured)

if __name__ == '__main__':
    app.wsgi_app = LoggingMiddleware(app.wsgi_app)
    app.run()
