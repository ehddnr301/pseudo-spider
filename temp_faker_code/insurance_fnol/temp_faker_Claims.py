


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Claim_ID": fake.random_int(min=1, max=10000),
            "FNOL_ID": fake.random_int(min=1, max=10000),
            "Effective_Date": fake.date_time_this_year().date()
        }
        data.append(record)
    return data
