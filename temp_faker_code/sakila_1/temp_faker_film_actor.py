


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "actor_id": random.randint(1, 65535),
            "film_id": random.randint(1, 65535),
            "last_update": fake.date_time_this_year()
        }
        data.append(record)
    return data
