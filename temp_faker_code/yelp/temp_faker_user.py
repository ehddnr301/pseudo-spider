


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "uid": random.randint(1, 1000),
            "user_id": fake.user_name(),
            "name": fake.name()
        }
        data.append(record)
    return data
