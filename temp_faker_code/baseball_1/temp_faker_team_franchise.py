


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "franchise_id": fake.uuid4(),
            "franchise_name": fake.company(),
            "active": random.choice(["Yes", "No"]),
            "na_assoc": fake.state_abbr()
        }
        data.append(record)
    return data
