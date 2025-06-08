


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Id": random.randint(1, 1000),
            "Firstname": fake.first_name(),
            "Lastname": fake.last_name()
        }
        data.append(record)
    return data
