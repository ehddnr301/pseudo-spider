


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "name": fake.first_name(),
            "friend": fake.first_name(),
            "year": random.randint(2000, 2022)
        }
        data.append(record)
    return data
