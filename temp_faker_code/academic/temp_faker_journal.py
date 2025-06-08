


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "homepage": fake.url(),
            "jid": fake.random_int(min=1, max=10000),
            "name": fake.name()
        }
        data.append(record)
    return data
