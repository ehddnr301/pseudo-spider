


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "uid": fake.random_int(min=1, max=10000),
            "name": fake.name(),
            "email": fake.email(),
            "partitionid": fake.random_int(min=1, max=100),
            "followers": fake.random_int(min=0, max=10000)
        }
        data.append(record)
    return data
