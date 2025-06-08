


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "endowment_id": _ + 1,
            "School_id": random.randint(1, 100),
            "donator_name": fake.name(),
            "amount": round(random.uniform(1000, 100000), 2)
        }
        data.append(record)
    return data
