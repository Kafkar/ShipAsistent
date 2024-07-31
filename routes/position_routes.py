from flask import Blueprint, render_template

bp = Blueprint('position', __name__)

@bp.route('/position')
def show_position():
    # This is a placeholder. You'll need to implement actual position tracking.
    position = {'latitude': 0, 'longitude': 0}
    return render_template('position.html', position=position)