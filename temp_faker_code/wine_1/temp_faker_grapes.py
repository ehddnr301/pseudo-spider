


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "ID": _ + 1,
            "Grape": fake.word(),
            "Color": random.choice(['Red', 'Green', 'Black', 'Purple', 'Yellow'])
        }
        data.append(record)
    return data
