


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "DepartmentID": random.randint(1, 1000),
            "Name": fake.word()[:30],
            "Head": random.randint(1, 1000)
        }
        data.append(record)
    return data
