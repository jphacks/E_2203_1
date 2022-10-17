from flask import Flask, request, jsonify
import mysql.connector as mydb

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
books = [{'name': 'EffectivePython', 'price': 3315}, {'name': 'Expert Python Programming', 'price': 3960}]

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
    return jsonify(book)

@app.route('/books/all', methods=['GET'])
def GetAll():
    return jsonify({'books': books})

if __name__ == '__main__':
    app.run()