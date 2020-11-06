import sentry_sdk

from bottle import Bottle
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://0798cf0e952f479480e8b65241658ba8@o472515.ingest.sentry.io/5506736",
    integrations=[BottleIntegration()]
)

app = Bottle()


@app.route('/fail')
def index_fail():
    raise RuntimeError("There is an error!")


@app.route('/success')
def index_success():
    return "Запрос успешный"


app.run(host='https://skillfactory-module-d2-10-home.herokuapp.com:8080', port=8080)
