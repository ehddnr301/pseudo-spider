


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Campus": random.randint(1, 10),
            "Year": fake.year(),
            "CampusFee": random.randint(1000, 5000)
        }
        data.append(record)
    return data
