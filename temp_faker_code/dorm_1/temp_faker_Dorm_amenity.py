


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "amenid": random.randint(1, 1000),
            "amenity_name": fake.word()[:25]
        }
        data.append(record)
    return data
