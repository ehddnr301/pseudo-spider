


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": random.randint(1, 1000),
            "msid": random.randint(1, 1000),
            "kid": random.randint(1, 1000)
        }
        data.append(record)
    return data
