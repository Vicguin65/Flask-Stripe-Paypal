from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


from flaskr.auth import login_required
from flaskr.db import get_db

from . import stripe_helper

import datetime

bp = Blueprint('subscribe', __name__)


@bp.route('/')
def index():
    status = None
    period_start = None
    period_end = None

    if g.user:
        subscriptions = stripe_helper.get_subscriptions(
            customer=g.user['stripe_id'])

        if len(subscriptions['data']) > 0:
            try:
                status = subscriptions['data'][0]['status']
                start_of_period = subscriptions['data'][0]['items']['data'][0]['current_period_start']
                end_of_period = subscriptions['data'][0]['items']['data'][0]['current_period_end']
                datetime_start = datetime.datetime.fromtimestamp(
                    start_of_period)
                datetime_end = datetime.datetime.fromtimestamp(end_of_period)

                period_start = datetime_start.strftime("%B %d, %Y")
                period_end = datetime_end.strftime("%B %d, %Y")

            except Exception as e:
                print(str(e))

    return render_template('subscribe/index.html', status=status, period_start=period_start, period_end=period_end)


@bp.route('/success')
def success():
    return render_template('subscribe/success.html')
