


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Order_ID": fake.random_int(min=1, max=1000),
            "Product_ID": fake.random_int(min=1, max=1000)
        }
        data.append(record)
    return data
