from flask import Flask, Blueprint, jsonify, request
borrow_entries = []
current_id = 1

borrow_bp = Blueprint('borrow_bp', __name__)

@borrow_bp.route("/borrow", methods =['POST'])

def borrow_book():
    global current_id
    data = {
        'id':current_id,
        'Tiltle':request.json.get['book_id'],
        'Author':request.json.get['author_name'],
        'boorrow_date':request.json.get('borrow_date',""),
        'return_date': request.json.get('return_date',"")
    }
    borrow_entries.append(data)
    current_id += 1
    return jsonify({'Recorded Entry':data}), 201
