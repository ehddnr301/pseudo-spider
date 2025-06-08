


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Year": fake.random_int(min=2000, max=2023),
            "Campus": fake.random_int(min=1, max=10),
            "Degrees": fake.random_int(min=1, max=100)
        }
        data.append(record)
    return data
