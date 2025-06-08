


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "state_name": fake.state(),
            "border": fake.country()
        }
        data.append(record)
    return data
