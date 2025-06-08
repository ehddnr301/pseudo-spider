


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "REGION_ID": random.randint(1, 99999),
            "REGION_NAME": fake.word()[:25]
        }
        data.append(record)
    return data
