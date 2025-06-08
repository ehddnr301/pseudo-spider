


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "authID": random.randint(1, 1000),
            "lname": fake.last_name(),
            "fname": fake.first_name()
        }
        data.append(record)
    return data
