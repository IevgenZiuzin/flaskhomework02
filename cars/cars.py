from flask import Blueprint, render_template

cars = Blueprint('cars', __name__, template_folder='templates')


@cars.route('/')
def cars_view():
    context = {
        'message': 'cars page content',
        'page_title': 'Cars',
        'subheader': [
            {
                'url': '#',
                'title': 'Toyota'
            },
            {
                'url': '#',
                'title': 'Honda'
            },
            {
                'url': '#',
                'title': 'Renault'
            },
        ]
    }
    return render_template('cars/cars.html', context=context)
