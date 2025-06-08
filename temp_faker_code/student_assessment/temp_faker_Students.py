


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "student_id": fake.unique.random_int(min=1, max=10000),
            "student_details": fake.name()
        }
        data.append(record)
    return data
