


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "source_u_id": fake.random_int(min=1, max=1000),
            "target_u_id": fake.random_int(min=1, max=1000),
            "trust": fake.random_int(min=0, max=10)
        }
        data.append(record)
    return data
