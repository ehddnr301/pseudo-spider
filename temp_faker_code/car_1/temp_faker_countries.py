


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "CountryId": _ + 1,
            "CountryName": fake.country(),
            "Continent": random.randint(1, 7)
        }
        data.append(record)
    return data
