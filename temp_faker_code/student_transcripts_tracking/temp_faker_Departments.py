


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "department_id": random.randint(1, 1000),
            "department_name": fake.word(),
            "department_description": fake.sentence(),
            "other_details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
