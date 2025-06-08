


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "dormid": random.randint(1, 100),
            "amenid": random.randint(1, 50)
        }
        data.append(record)
    return data
