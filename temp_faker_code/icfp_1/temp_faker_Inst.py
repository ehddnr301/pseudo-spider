


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "instID": fake.random_int(min=1, max=1000),
            "name": fake.name(),
            "country": fake.country()
        }
        data.append(record)
    return data
