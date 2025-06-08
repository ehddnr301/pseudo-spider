


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Essn": fake.random_int(min=1000, max=9999),
            "Pno": fake.random_int(min=1, max=100),
            "Hours": round(random.uniform(1, 40), 2)
        }
        data.append(record)
    return data
