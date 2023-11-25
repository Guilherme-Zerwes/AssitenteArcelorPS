from flask import Flask
from views import view
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.register_blueprint(view, url_prefix='/')

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

if __name__ == '__main__':
    app.run(debug=True)