


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "BlockFloor": random.randint(1, 10),
            "BlockCode": random.randint(1000, 9999)
        }
        data.append(record)
    return data
