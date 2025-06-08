


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "building": fake.word()[:15],
            "room_number": fake.random_int(min=1, max=9999999),
            "capacity": fake.random_int(min=1, max=9999)
        }
        data.append(record)
    return data
