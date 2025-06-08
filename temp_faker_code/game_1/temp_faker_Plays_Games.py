


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "StuID": fake.random_int(min=1, max=1000),
            "GameID": fake.random_int(min=1, max=100),
            "Hours_Played": fake.random_int(min=1, max=100)
        }
        data.append(record)
    return data
