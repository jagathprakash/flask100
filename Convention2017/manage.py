#!/usr/bin/env python
import os

from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)