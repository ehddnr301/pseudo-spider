


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Artwork_ID": fake.random_int(min=1, max=1000),
            "Festival_ID": fake.random_int(min=1, max=100),
            "Result": fake.word()
        }
        data.append(record)
    return data
