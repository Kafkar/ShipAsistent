from flask import Blueprint, render_template
from datetime import datetime

bp = Blueprint('time', __name__)

@bp.route('/time')
def show_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    return render_template('time.html', time=current_time)