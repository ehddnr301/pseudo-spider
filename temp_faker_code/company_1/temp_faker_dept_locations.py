


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Dnumber": random.randint(1, 100),
            "Dlocation": fake.city()
        }
        data.append(record)
    return data
