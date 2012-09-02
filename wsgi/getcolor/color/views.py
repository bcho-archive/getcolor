#coding: utf-8

from flask import Blueprint
from flask import request
from flask import jsonify, json

from .utils import add_color
from .utils import search_color_by_keyword

app = Blueprint('color', __name__)


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            return jsonify({'new': add_color(request.json)})
        else:
            return 'Not json', 500


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.headers['Content-Type'] == 'application/json':
        keyword = request.json['keyword']
        limit = request.json.get('limit', 100)
        ret, count = search_color_by_keyword(keyword, limit)
        return jsonify({'result': ret, 'count': count})
    else:
        return 'Not json', 500
