#encoding:utf-8

from flask import Blueprint

index_blu = Blueprint("index_blu",__name__)

from .view import *