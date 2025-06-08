


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "staff_id": random.randint(1, 1000),
            "gender": random.choice(['M', 'F']),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email_address": fake.email(),
            "phone_number": fake.phone_number()
        }
        data.append(record)
    return data
