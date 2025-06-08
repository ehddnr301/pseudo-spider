


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Country_id": fake.random_int(min=1, max=1000),
            "Country_name": fake.country(),
            "Capital": fake.city(),
            "Official_native_language": fake.language_name()
        }
        data.append(record)
    return data
