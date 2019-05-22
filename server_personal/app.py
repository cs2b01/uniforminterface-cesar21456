from flask import Flask, render_template, session, request, url_for, Response, redirect
from database import connector
from model import entities
import json

app = Flask(__name__)
db = connector.Manager()
engine = db.createEngine()

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/users')
def users():
    db_session = db.getSession(engine)
    users = db_session.query(entities.user)
    data = users[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype = 'application/json')


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('0.0.0.0'))
