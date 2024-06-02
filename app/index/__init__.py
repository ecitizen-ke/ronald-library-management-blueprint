from flask import Flask, Blueprint, jsonify

index_bp = Blueprint('index_bp', __name__,)


@index_bp.route('/', methods = ['GET'])
def index():
    return '<h1> Welcome to Library Management System </h1>'


