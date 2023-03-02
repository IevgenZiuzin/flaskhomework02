from flask import Flask, render_template

from song.song import song
from cars.cars import cars
from weekday.weekday import weekday
from books.books import books
from headphones.headphones import headphones


app = Flask(__name__)
app.register_blueprint(song, url_prefix='/song')
app.register_blueprint(cars, url_prefix='/cars')
app.register_blueprint(weekday, url_prefix='/weekday')
app.register_blueprint(books, url_prefix='/books')
app.register_blueprint(headphones, url_prefix='/headphones')


@app.route('/')
def index():
    context = {
        'message': 'home page content',
        'page_title': 'Home'
    }
    return render_template('index.html', context=context)


if __name__ == '__main__':
    app.run(debug=True, port=8000)