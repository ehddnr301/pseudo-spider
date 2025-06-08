


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Editor_ID": _ + 1,
            "Name": fake.name(),
            "Age": round(random.uniform(20, 60), 2)
        }
        data.append(record)
    return data
