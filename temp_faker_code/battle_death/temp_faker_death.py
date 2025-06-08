


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "caused_by_ship_id": random.randint(1, 100),
            "id": fake.unique.random_int(min=1, max=1000),
            "note": fake.sentence(),
            "killed": random.randint(0, 100),
            "injured": random.randint(0, 100)
        }
        data.append(record)
    return data
