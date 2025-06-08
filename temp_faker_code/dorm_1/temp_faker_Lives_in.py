


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "stuid": fake.random_int(min=1, max=1000),
            "dormid": fake.random_int(min=1, max=100),
            "room_number": fake.random_int(min=1, max=10)
        }
        data.append(record)
    return data
