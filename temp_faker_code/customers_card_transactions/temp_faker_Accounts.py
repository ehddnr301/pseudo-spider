


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "account_id": fake.random_int(min=1, max=1000),
            "customer_id": fake.random_int(min=1, max=1000),
            "account_name": fake.company()[:50],
            "other_account_details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
