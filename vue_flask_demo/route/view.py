#encoding:utf-8

from . import index_blu
import json

data_list = list()
with open("./data.json", "r", encoding="utf-8") as f:
    data_str = f.read()
    data = json.loads(data_str)
    for key, value in data.items():
        data_list.append(dict(key=key, value=value))


@index_blu.route("/index")
def index():
    return dict(code=1, message="Success", data=data_list)


@index_blu.route("/get_data")
def get_data():
    return ""
