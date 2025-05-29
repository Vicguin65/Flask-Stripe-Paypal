from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('subscribe', __name__)


@bp.route('/')
def index():
    return render_template('subscribe/index.html')


@bp.route('/success')
def success():
    return render_template('subscribe/success.html')
