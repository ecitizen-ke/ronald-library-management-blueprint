from flask import Flask, jsonify, request, abort    
from app.addbook import borrow_bp
from app.returnbook import returnbook_bp
from app.viewbook import view_bp
from app.index import index_bp
from  dotenv import load_dotenv
load_dotenv()

borrow_entries = []


app = Flask(__name__)
app.register_blueprint(index_bp)
app.register_blueprint(borrow_bp)
app.register_blueprint(returnbook_bp)
app.register_blueprint(view_bp)

if __name__== '__main__':
    app.run(debug= True)
