


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "customer_id": random.randint(1, 1000),
            "payment_method": fake.random_element(elements=("Credit Card", "Debit Card", "PayPal")),
            "customer_name": fake.name(),
            "date_became_customer": fake.date_time_this_year(),
            "other_customer_details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
