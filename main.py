from flask import Flask, render_template, url_for

from song.song import song
from cars.cars import cars
from weekday.weekday import weekday


app = Flask(__name__)
app.register_blueprint(song, url_prefix='/song')
app.register_blueprint(cars, url_prefix='/cars')
app.register_blueprint(weekday, url_prefix='/weekday')


@app.route('/')
def index():
    context = {
        'message': 'home page content',
        'page_title': 'Home'
    }
    return render_template('index.html', context=context)


@app.errorhandler(404)
def page_not_found(e):
    context = {
        'page_title': '404',
    }
    return render_template('404.html', context=context), 404


@app.errorhandler(500)
def internal_server_error(e):
    context = {
        'page_title': '500',
    }
    return render_template('500.html', context=context), 500


if __name__ == '__main__':
    app.run(debug=True, port=8000)
