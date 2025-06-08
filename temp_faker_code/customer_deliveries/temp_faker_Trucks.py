


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "truck_id": random.randint(1, 1000),
            "truck_licence_number": fake.license_plate(),
            "truck_details": fake.sentence()
        }
        data.append(record)
    return data
