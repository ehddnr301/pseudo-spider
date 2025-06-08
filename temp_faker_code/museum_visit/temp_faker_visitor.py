


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "ID": _ + 1,
            "Name": fake.name(),
            "Level_of_membership": random.randint(1, 5),
            "Age": random.randint(18, 70)
        }
        data.append(record)
    return data
