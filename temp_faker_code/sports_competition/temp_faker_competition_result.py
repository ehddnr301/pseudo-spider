


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Competition_ID": fake.random_int(min=1, max=1000),
            "Club_ID_1": fake.random_int(min=1, max=100),
            "Club_ID_2": fake.random_int(min=1, max=100),
            "Score": f"{fake.random_int(min=0, max=5)}:{fake.random_int(min=0, max=5)}"
        }
        data.append(record)
    return data
