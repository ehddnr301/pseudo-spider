


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "MakeId": random.randint(1, 1000),
            "Model": fake.word(),
            "Make": fake.company()
        }
        data.append(record)
    return data
