from flask import Blueprint, render_template, url_for, redirect

cars = Blueprint('cars', __name__, template_folder='templates', static_folder='static')


@cars.route('/')
def cars_view():
    context = {
        'message': 'click on brands above',
        'page_title': 'Cars',
        'subheader': [
            {
                'url': url_for('cars.cars_brands', brand='toyota'),
                'title': 'Toyota'
            },
            {
                'url': url_for('cars.cars_brands', brand='honda'),
                'title': 'Honda'
            },
            {
                'url': url_for('cars.cars_brands', brand='renault'),
                'title': 'Renault'
            },
        ]
    }
    return render_template('cars/cars.html', context=context)


@cars.route('/<string:brand>')
def cars_brands(brand):
    brands = {
        'toyota': {
            'model': 'GR Corolla',
            'image_path': '2023_Toyota_GR_Corolla,_front_NYIAS_2022.jpg'
        },
        'honda': {
            'model': 'Accord Touring Hybrid',
            'image_path': 'Honda_Accord_Touring_Hybrid.jpg'
        },
        'renault': {
            'model': 'Clio Iconic',
            'image_path': '2019_Renault_Clio_Iconic_TCE_1.0_Front.jpg'
        }
    }
    if brand not in brands:
        return redirect(url_for('index'))
    context = {
        'car': brands[brand],
        'page_title': brand.title(),
        'subheader': [
            {
                'url': url_for('cars.cars_brands', brand='toyota'),
                'title': 'Toyota'
            },
            {
                'url': url_for('cars.cars_brands', brand='honda'),
                'title': 'Honda'
            },
            {
                'url': url_for('cars.cars_brands', brand='renault'),
                'title': 'Renault'
            },
        ]
    }
    return render_template('cars/cars.html', context=context)
