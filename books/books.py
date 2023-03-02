from flask import Blueprint, request, render_template

books = Blueprint('books', __name__, template_folder='templates')


@books.route('/', methods=['GET', 'POST'])
def books_view():
    print(request.values.get('param1'))
    context = {
        'message': 'books page content',
        'page_title': 'Books',
    }
    return render_template('books/books.html', context=context)
