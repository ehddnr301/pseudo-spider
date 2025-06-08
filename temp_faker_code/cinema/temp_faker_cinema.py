


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Cinema_ID": fake.unique.random_int(min=1, max=1000),
            "Name": fake.company(),
            "Openning_year": fake.year(),
            "Capacity": fake.random_int(min=50, max=500),
            "Location": fake.city()
        }
        data.append(record)
    return data
