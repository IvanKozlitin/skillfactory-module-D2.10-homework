import os
import sentry_sdk

from bottle import Bottle, run, error, HTTPResponse, route
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://0798cf0e952f479480e8b65241658ba8@o472515.ingest.sentry.io/5506736",
    integrations=[BottleIntegration()]
)

class NotFound(Exception):
    """
    Используется для идентификации ошибки 404, для последующей отправки в sentry.io
    """
    pass

@error(404)
def error404(error):
    raise NotFound("Страница не найдена")

@route("/")
def hello_page():
    return HTTPResponse(200, "Привет!")

@route('/fail')
def index_fail():
    raise RuntimeError("There is an error!")


@route('/success')
def index_success():
    return HTTPResponse(200, "Запрос успешный")

if os.environ.get('SERVER_URL') == 'https://skillfactory-module-d2-10-home.herokuapp.com':
    run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        server='gunicorn',
        workers=3
    )
else:
    run(
        host='localhost',
        port=8080,
        debug=True
    )