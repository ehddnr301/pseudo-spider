


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "People_ID": _ + 1,
            "Name": fake.name(),
            "Country": fake.country(),
            "Is_Male": random.choice(["Yes", "No"]),
            "Age": random.randint(18, 80)
        }
        data.append(record)
    return data
