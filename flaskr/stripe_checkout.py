from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
from . import stripe_helper


bp = Blueprint('stripe_checkout', __name__)


@bp.route('/create-checkout-session', methods=('POST'))
@login_required
def create_checkout_session():
    try:
        stripe_client = stripe_helper.get_stripe_client()
        checkout_session = stripe_client.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, price_1234) of the product you want to sell
                    'price': '{{PRICE_ID}}',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=url_for('index') + '/success.html',
            cancel_url=url_for('index') + '/cancel.html',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)
