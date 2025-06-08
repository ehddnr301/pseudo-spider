


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "transaction_id": fake.random_int(min=1, max=10000),
            "lot_id": fake.random_int(min=1, max=10000)
        }
        data.append(record)
    return data
