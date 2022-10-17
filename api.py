from flask import Flask, request, jsonify
import mysql.connector as mydb
from db import SelectAll, insert, dbinit

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
books = [{'name': 'EffectivePython', 'price': 3315}, {'name': 'Expert Python Programming', 'price': 3960}]

dbinit()

@app.route('/books', methods=['POST'])
def post_json():
    #受け取る
    json = request.get_json()
    #パースする
    name = json['name']
    price = json['price']
    book = {'name': name, 'price': price}
    books.append(book)

    book_id = len(books)
    book['id'] = book_id

    insert (book_id, name, price)

    return jsonify(book)
    

@app.route('/books/all', methods=['GET'])
def GetAll():
    return jsonify({'books': SelectAll()})

if __name__ == '__main__':
    app.run()