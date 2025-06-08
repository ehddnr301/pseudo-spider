


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "supplier_id": random.randint(1, 1000),
            "supplier_name": fake.company(),
            "supplier_phone": fake.phone_number()
        }
        data.append(record)
    return data
