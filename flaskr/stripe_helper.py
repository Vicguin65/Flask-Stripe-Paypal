import stripe

import os
from dotenv import load_dotenv

load_dotenv()


def get_stripe_client():
    stripe.api_key = os.getenv("SECRET_KEY")
    return stripe


def create_stripe_customer(name: str, email: str) -> str:
    stripe.api_key = os.getenv("SECRET_KEY")
    customer = stripe.Customer.create(
        name=name,
        email=email
    )
    print('we got', customer['id'])
    return customer['id']
