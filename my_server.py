import os
import sentry_sdk
from bottle import run, route, error, HTTPResponse
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://0798cf0e952f479480e8b65241658ba8@o472515.ingest.sentry.io/5506736",
    integrations=[BottleIntegration()]
)


@error(404)
def error404():
    return HTTPResponse(status=404, body="Страница не найдена")


@route("/")
def hello_page():
    return HTTPResponse(status=200, body="Привет!")


@route('/fail')
def index_fail():
    raise RuntimeError("There is an error!")


@route('/success')
def index_success():
    return HTTPResponse(status=200, body="Запрос успешный")


if __name__ == "__main__":
    run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        server='gunicorn',
        workers=3
    )
