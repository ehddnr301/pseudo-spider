


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Program_ID": fake.random_int(min=1, max=1000),
            "Name": fake.catch_phrase(),
            "Origin": fake.country(),
            "Launch": fake.date_time_this_year().timestamp(),
            "Owner": fake.name()
        }
        data.append(record)
    return data
