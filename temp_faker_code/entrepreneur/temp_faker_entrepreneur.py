


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Entrepreneur_ID": _ + 1,
            "People_ID": random.randint(1, 100),
            "Company": fake.company(),
            "Money_Requested": round(random.uniform(1000, 100000), 2),
            "Investor": fake.name()
        }
        data.append(record)
    return data
