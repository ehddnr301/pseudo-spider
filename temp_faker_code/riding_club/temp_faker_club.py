


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Club_ID": _ + 1,
            "Club_name": fake.company(),
            "Region": fake.city(),
            "Start_year": random.randint(1900, 2023)
        }
        data.append(record)
    return data
