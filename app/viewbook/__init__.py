from flask import Flask, jsonify, Blueprint, request
from app.addbook import borrow_entries

view_bp = Blueprint('view_bp', __name__)

@view_bp.route('/view', methods = ['GET'])
def view_books():
    return jsonify({'Borrowed Books':borrow_entries}), 201
