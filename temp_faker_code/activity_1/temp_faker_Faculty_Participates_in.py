


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "FacID": random.randint(1, 100),
            "actid": random.randint(1, 100)
        }
        data.append(record)
    return data
