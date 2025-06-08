


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "park_id": fake.uuid4(),
            "park_name": fake.name(),
            "park_alias": fake.word(),
            "city": fake.city(),
            "state": fake.state(),
            "country": fake.country()
        }
        data.append(record)
    return data
