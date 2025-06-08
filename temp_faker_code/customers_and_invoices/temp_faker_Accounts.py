


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "account_id": random.randint(1, 1000),
            "customer_id": random.randint(1, 1000),
            "date_account_opened": fake.date_time_this_year(),
            "account_name": fake.name()[:50],
            "other_account_details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
