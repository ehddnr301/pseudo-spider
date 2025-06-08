


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Dname": fake.word(),
            "Dnumber": fake.random_int(min=1, max=100),
            "Mgr_ssn": fake.random_int(min=100000000, max=999999999),
            "Mgr_start_date": fake.date_time_this_year().strftime("%Y-%m-%d")
        }
        data.append(record)
    return data
