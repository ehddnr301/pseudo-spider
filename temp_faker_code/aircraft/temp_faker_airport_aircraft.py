


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "ID": random.randint(1, 1000),
            "Airport_ID": random.randint(1, 100),
            "Aircraft_ID": random.randint(1, 100)
        }
        data.append(record)
    return data
