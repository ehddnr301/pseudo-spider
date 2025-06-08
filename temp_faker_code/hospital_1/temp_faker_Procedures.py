


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Code": random.randint(1, 1000),
            "Name": fake.word()[:30],
            "Cost": round(random.uniform(10.0, 500.0), 2)
        }
        data.append(record)
    return data
