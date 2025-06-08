


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "employee_id": random.randint(1, 1000),
            "employee_address_id": random.randint(1, 1000),
            "employee_name": fake.name(),
            "employee_phone": fake.phone_number()
        }
        data.append(record)
    return data
