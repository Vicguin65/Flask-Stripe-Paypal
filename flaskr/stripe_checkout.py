from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
from . import stripe_helper


bp = Blueprint('stripe_checkout', __name__)


@bp.route('/create-checkout-session', methods=('POST', 'GET'))
@login_required
def create_checkout_session():
    try:
        stripe_client = stripe_helper.get_stripe_client()
        checkout_session = stripe_client.checkout.Session.create(
            customer=g.user['stripe_id'],
            line_items=[
                {
                    'price': 'price_1RRjCHQnnAtAO4Wp4bXSXa7L',
                    'quantity': 1,
                },
            ],
            mode='subscription',
            success_url='http://localhost:5000/success',
            cancel_url='http://localhost:5000',
        )
    except Exception as e:
        print('errored')
        print(url_for('index'))
        return str(e)

    return redirect(checkout_session.url, code=303)
