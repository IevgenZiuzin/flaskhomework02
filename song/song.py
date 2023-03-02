from flask import Blueprint, render_template

song = Blueprint('song', __name__, template_folder='templates')


@song.route('/')
def song_view():
    context = {
        'message': 'song line page content',
        'page_title': 'Song',
        'subheader': [
            {
                'url': '#',
                'title': 'en'
            },
            {
                'url': '#',
                'title': 'fr'
            },
            {
                'url': '#',
                'title': 'de'
            },
        ]
    }
    return render_template('song/song.html', context=context)
