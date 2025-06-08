


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Market_ID": fake.random_int(min=1, max=1000),
            "Country": fake.country(),
            "Number_cities": fake.random_int(min=1, max=100)
        }
        data.append(record)
    return data
