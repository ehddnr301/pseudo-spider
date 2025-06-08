


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "architect_id": random.randint(1, 100),
            "id": _ + 1,
            "name": fake.name(),
            "location": fake.city(),
            "length_meters": round(random.uniform(10.0, 1000.0), 2),
            "length_feet": round(random.uniform(32.8, 3280.84), 2)
        }
        data.append(record)
    return data
