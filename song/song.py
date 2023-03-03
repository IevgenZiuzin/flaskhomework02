from flask import Blueprint, render_template, url_for, redirect

song = Blueprint('song', __name__, template_folder='templates')


@song.route('/')
def song_view():
    return redirect(url_for('song.song_translations', lang='en'))


@song.route('/<string:lang>')
def song_translations(lang):
    line = {
        'en': 'i am the walrus',
        'fr': 'je suis le morse',
        'de': 'ich bin das Walroß'
    }
    if lang not in line:
        return redirect(url_for('index'))
    context = {
        'message': line[lang],
        'page_title': 'Song',
        'subheader': [
            {
                'url': url_for('song.song_translations', lang='en'),
                'title': 'en'
            },
            {
                'url': url_for('song.song_translations', lang='fr'),
                'title': 'fr'
            },
            {
                'url': url_for('song.song_translations', lang='de'),
                'title': 'de'
            },
        ]
    }
    return render_template('song/song.html', context=context)
