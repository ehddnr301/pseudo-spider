


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "order_item_id": fake.random_int(min=1, max=10000),
            "order_id": fake.random_int(min=1, max=1000),
            "product_id": fake.random_int(min=1, max=500)
        }
        data.append(record)
    return data
