from flask import Flask
from flask import Response, request
flask_app = Flask('flaskapp')


@flask_app.route('/')
def hello_world():
    content = request.get_json(silent=True)
    print content
    return Response("aaaaaaa",  mimetype='text/html')



app = flask_app.wsgi_app