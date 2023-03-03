from flask import Blueprint, render_template, request
import datetime

weekday = Blueprint('weekday', __name__, template_folder='templates', static_folder='static')


@weekday.route('/', methods=['GET', 'POST'])
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
    next_day = {
        'Sunday': 'Monday',
        'Monday': 'Tuesday',
        'Tuesday': 'Wednesday',
        'Wednesday': 'Thursday',
        'Thursday': 'Friday',
        'Friday': 'Saturday',
        'Saturday': 'Sunday'
    }
    if request.method == 'POST':
        current_day = request.form.get('day')
        day = next_day[current_day]
    context = {
        'page_title': 'Weekday',
        'day': day,
        'color': colors[day]
    }
    return render_template('weekday/weekday.html', context=context)
