


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "course_id": fake.bothify(text='??######'),
            "prereq_id": fake.bothify(text='??######')
        }
        data.append(record)
    return data
