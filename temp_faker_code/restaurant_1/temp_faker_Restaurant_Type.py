


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "ResTypeID": random.randint(1, 1000),
            "ResTypeName": fake.word()[:40],
            "ResTypeDescription": fake.sentence()[:100]
        }
        data.append(record)
    return data
