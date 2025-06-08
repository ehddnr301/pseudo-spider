


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Captain_ID": fake.random_int(min=1, max=1000),
            "Name": fake.name(),
            "Ship_ID": fake.random_int(min=1, max=100),
            "age": str(fake.random_int(min=20, max=60)),
            "Class": fake.word(),
            "Rank": fake.word()
        }
        data.append(record)
    return data
