


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "staff_id": random.randint(1, 1000),
            "employer_organisation_id": random.randint(1, 100),
            "staff_details": fake.name()
        }
        data.append(record)
    return data
