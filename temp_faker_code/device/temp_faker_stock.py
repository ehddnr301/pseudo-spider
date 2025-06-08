


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Shop_ID": fake.random_int(min=1, max=100),
            "Device_ID": fake.random_int(min=1, max=100),
            "Quantity": fake.random_int(min=1, max=50)
        }
        data.append(record)
    return data
