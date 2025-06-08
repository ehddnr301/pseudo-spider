


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Course_ID": fake.random_int(min=1, max=100),
            "Teacher_ID": fake.random_int(min=1, max=100),
            "Grade": fake.random_int(min=1, max=12)
        }
        data.append(record)
    return data
