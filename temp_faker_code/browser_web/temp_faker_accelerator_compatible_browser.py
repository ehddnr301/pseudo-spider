


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "accelerator_id": fake.random_int(min=1, max=1000),
            "browser_id": fake.random_int(min=1, max=1000),
            "compatible_since_year": fake.random_int(min=2000, max=2023)
        }
        data.append(record)
    return data
