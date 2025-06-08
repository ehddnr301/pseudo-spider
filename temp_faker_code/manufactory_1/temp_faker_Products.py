


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Code": random.randint(1, 1000),
            "Name": fake.word(),
            "Price": round(random.uniform(1.0, 1000.0), 2),
            "Manufacturer": random.randint(1, 100)
        }
        data.append(record)
    return data
