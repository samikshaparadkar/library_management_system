from flask import Flask, render_template

app = Flask(__name__)

# Dummy data for books and members (for simplicity)
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1", "quantity": 10},
    {"id": 2, "title": "Book 2", "author": "Author 2", "quantity": 5},
]

members = [
    {"id": 1, "name": "Member 1", "contact": "Contact 1"},
    {"id": 2, "name": "Member 2", "contact": "Contact 2"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books')
def list_books():
    return render_template('books.html', books=books)

@app.route('/members')
def list_members():
    return render_template('members.html', members=members)

if __name__ == '__main__':
    app.run(debug=True)
