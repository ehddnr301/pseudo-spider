


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": random.randint(1, 1000),
            "name": fake.company(),
            "country_code": fake.country_code()
        }
        data.append(record)
    return data
