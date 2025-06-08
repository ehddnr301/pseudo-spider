


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "person_address_id": fake.random_int(min=1, max=1000),
            "person_id": fake.random_int(min=1, max=1000),
            "address_id": fake.random_int(min=1, max=1000),
            "date_from": fake.date_time_this_year(),
            "date_to": fake.date_time_this_year()
        }
        data.append(record)
    return data
