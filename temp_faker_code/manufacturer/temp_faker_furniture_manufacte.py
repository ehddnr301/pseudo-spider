


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Manufacturer_ID": fake.random_int(min=1, max=1000),
            "Furniture_ID": fake.random_int(min=1, max=1000),
            "Price_in_Dollar": round(fake.random_number(digits=3) + fake.random.random(), 2)
        }
        data.append(record)
    return data
