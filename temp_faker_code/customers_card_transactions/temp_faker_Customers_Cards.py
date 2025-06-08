


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "card_id": _ + 1,
            "customer_id": fake.random_int(min=1, max=1000),
            "card_type_code": fake.random_element(elements=("VISA", "MASTERCARD", "AMEX")),
            "card_number": fake.credit_card_number(),
            "date_valid_from": fake.date_time_this_year(),
            "date_valid_to": fake.date_time_this_year(),
            "other_card_details": fake.sentence()
        }
        data.append(record)
    return data
