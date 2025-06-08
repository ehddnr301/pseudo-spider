


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Nurse": fake.random_int(min=1, max=100),
            "BlockFloor": fake.random_int(min=1, max=10),
            "BlockCode": fake.random_int(min=1, max=5),
            "OnCallStart": fake.date_time_this_year(),
            "OnCallEnd": fake.date_time_this_year()
        }
        data.append(record)
    return data
