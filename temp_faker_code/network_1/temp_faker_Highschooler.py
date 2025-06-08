


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "ID": _ + 1,
            "name": fake.name(),
            "grade": random.randint(1, 12)
        }
        data.append(record)
    return data
