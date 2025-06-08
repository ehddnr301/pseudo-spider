


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": fake.random_int(min=1, max=1000000),
            "uid": fake.random_int(min=1, max=100000),
            "text": fake.text(max_nb_chars=140),
            "createdate": fake.date_time_this_year()
        }
        data.append(record)
    return data
