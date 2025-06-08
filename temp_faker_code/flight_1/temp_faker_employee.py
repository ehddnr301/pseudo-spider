


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "eid": fake.random_int(min=1, max=999999999),
            "name": fake.name(),
            "salary": round(fake.random_number(digits=8), 2)
        }
        data.append(record)
    return data
