


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "pID": random.randint(1, 99999),
            "pName": fake.name(),
            "yCard": fake.random_element(elements=('A', 'B', 'C')),
            "HS": random.randint(0, 99999)
        }
        data.append(record)
    return data
