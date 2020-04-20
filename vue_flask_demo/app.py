#encoding: utf-8
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')
from .route.view import index_blu
app.register_blueprint(index_blu, url_prefix='')

# @app.route('/index')
# def index_charts():
#     return dict(code=1, message="Success", data=data_list)


if __name__ == '__main__':
    app.run()
