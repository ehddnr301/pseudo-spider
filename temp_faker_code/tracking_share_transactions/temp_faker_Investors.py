


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "investor_id": fake.random_int(min=1, max=1000),
            "Investor_details": fake.name()
        }
        data.append(record)
    return data
