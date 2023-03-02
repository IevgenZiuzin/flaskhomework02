from flask import Blueprint, render_template
import datetime

weekday = Blueprint('weekday', __name__, template_folder='templates', static_folder='static')


@weekday.route('/')
def weekday_view():
    day = datetime.datetime.now().strftime('%A')
    colors = {
        'Sunday': 'bg-danger',
        'Monday': 'bg-lite',
        'Tuesday': 'bg-info',
        'Wednesday': 'bg-warning',
        'Thursday': 'bg-primary',
        'Friday': 'bg-success',
        'Saturday': 'bg-secondary'
    }
    context = {
        'page_title': 'Weekday',
        'day': day,
        'color': colors[day]
    }
    return render_template('weekday/index.html', context=context)
