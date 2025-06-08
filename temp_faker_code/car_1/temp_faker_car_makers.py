


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Id": _ + 1,
            "Maker": fake.company(),
            "FullName": fake.name(),
            "Country": fake.country()
        }
        data.append(record)
    return data
