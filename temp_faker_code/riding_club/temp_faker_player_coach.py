


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Player_ID": fake.random_int(min=1, max=1000),
            "Coach_ID": fake.random_int(min=1, max=100),
            "Starting_year": fake.date_time_this_year().year
        }
        data.append(record)
    return data
