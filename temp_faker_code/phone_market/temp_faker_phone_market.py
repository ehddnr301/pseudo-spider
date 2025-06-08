


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Market_ID": random.randint(1, 100),
            "Phone_ID": fake.uuid4(),
            "Num_of_stock": random.randint(1, 100)
        }
        data.append(record)
    return data
