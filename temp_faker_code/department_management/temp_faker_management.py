


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "department_ID": fake.random_int(min=1, max=100),
            "head_ID": fake.random_int(min=1, max=100),
            "temporary_acting": fake.sentence()
        }
        data.append(record)
    return data
