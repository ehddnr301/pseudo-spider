


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "StuID": fake.unique.random_int(min=1, max=1000),
            "LName": fake.last_name()[:12],
            "Fname": fake.first_name()[:12],
            "Age": fake.random_int(min=18, max=30),
            "Sex": random.choice(['M', 'F']),
            "Major": fake.random_int(min=1, max=10),
            "Advisor": fake.random_int(min=1, max=10),
            "city_code": fake.city()[:3].upper()
        }
        data.append(record)
    return data
