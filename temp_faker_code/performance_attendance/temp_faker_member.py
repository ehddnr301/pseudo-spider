


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Member_ID": fake.uuid4(),
            "Name": fake.name(),
            "Nationality": fake.country(),
            "Role": random.choice(["Admin", "User", "Guest"])
        }
        data.append(record)
    return data
