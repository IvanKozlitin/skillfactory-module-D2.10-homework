import os
import sentry_sdk
from bottle import run, route, HTTPResponse
from sentry_sdk.integrations.bottle import BottleIntegration
from userconf import USER_DSN

sentry_sdk.init(
    dsn=USER_DSN,
    integrations=[BottleIntegration()]
)


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
