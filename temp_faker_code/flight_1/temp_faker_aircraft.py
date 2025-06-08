


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "aid": random.randint(1, 999999999),
            "name": fake.word()[:30],
            "distance": random.randint(1, 999999)
        }
        data.append(record)
    return data
