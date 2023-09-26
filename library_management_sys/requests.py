import requests

@app.route('/import-books', methods=['POST'])
def import_books():
    num_books = request.form['num_books']
    title = request.form['title']
    author = request.form['author']

    # Request to the Frappe API for getting dataset
    api_url = 'https://frappe.io/api/method/frappe-library'
    params = {
        'page': 2,
        'title': title,
        'author': author
    }
    response = requests.get(api_url, params=params)
    return redirect('/books')  
