from flask import Blueprint, render_template

headphones = Blueprint('headphones', __name__, template_folder='templates')


@headphones.route('/')
def headphones_view():
    context = {
        'message': 'headphones page content',
        'page_title': 'Headphones',
    }
    return render_template('headphones/headphones.html', context=context)
