


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "LastName": fake.last_name(),
            "FirstName": fake.first_name(),
            "Classroom": random.randint(1, 10)
        }
        data.append(record)
    return data
