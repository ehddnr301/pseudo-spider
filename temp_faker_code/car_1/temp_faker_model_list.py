


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "ModelId": random.randint(1, 1000),
            "Maker": random.randint(1, 100),
            "Model": fake.word()
        }
        data.append(record)
    return data
