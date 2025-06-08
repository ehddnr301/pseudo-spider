


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Competition_ID": fake.unique.random_int(min=1, max=1000),
            "Year": fake.year(),
            "Competition_type": fake.word(),
            "Country": fake.country()
        }
        data.append(record)
    return data
