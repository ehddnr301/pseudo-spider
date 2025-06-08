


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": random.randint(1, 1000),
            "name": fake.word(),
            "Trade_Name": fake.word(),
            "FDA_approved": fake.date_this_year().strftime("%Y-%m-%d")
        }
        data.append(record)
    return data
