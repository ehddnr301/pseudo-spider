


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "ContId": random.randint(1, 1000),
            "Continent": fake.continent()
        }
        data.append(record)
    return data
