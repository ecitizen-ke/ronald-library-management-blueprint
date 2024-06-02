from flask import Flask, jsonify, request, Blueprint
from app.addbook import borrow_entries, current_id
returnbook_bp = Blueprint('returnbook_bp', __name__)


@returnbook_bp.route('/retrun/<int:entry_id>', methods = ['DELETE'])
def return_book(entry_id):
    global borrow_entries
    global current_id
    for entry in borrow_entries:
        iterator = iter(entry.items())
        key_value = next(iterator)
        id = key_value[1]
        if entry_id == id:
            return print(f'Entry No: {entry_id} has been successfully deleted') 
    return 'Error!! Wrong entry', 404

