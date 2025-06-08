


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "catalog_entry_id": fake.random_int(min=1, max=1000),
            "catalog_level_number": fake.random_int(min=1, max=10),
            "attribute_id": fake.random_int(min=1, max=100),
            "attribute_value": fake.word()
        }
        data.append(record)
    return data
