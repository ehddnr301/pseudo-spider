


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    records = []
    for _ in range(num_records):
        record = {
            "ID": fake.random_int(min=1, max=1000),
            "Result": fake.word(),
            "Swimmer_ID": fake.random_int(min=1, max=100),
            "Event_ID": fake.random_int(min=1, max=50)
        }
        records.append(record)
    return records
