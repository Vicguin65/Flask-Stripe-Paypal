import stripe

import os
from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.getenv("SECRET_KEY")


def get_stripe_client():
    stripe.api_key = os.getenv("SECRET_KEY")
    return stripe


def create_stripe_customer(name: str, email: str) -> str:
    customer = stripe.Customer.create(
        name=name,
        email=email
    )
    return customer['id']


def get_subscriptions(customer: str):
    subscriptions = stripe.Subscription.list(customer=customer, limit=10)
    return subscriptions
