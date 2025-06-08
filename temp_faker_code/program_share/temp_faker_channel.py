


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Channel_ID": _ + 1,
            "Name": fake.company(),
            "Owner": fake.name(),
            "Share_in_percent": round(random.uniform(0, 100), 2),
            "Rating_in_percent": round(random.uniform(0, 100), 2)
        }
        data.append(record)
    return data
