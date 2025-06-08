


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        record = {
            "No": i + 1,
            "Appelation": fake.word(),
            "County": fake.city(),
            "State": fake.state(),
            "Area": fake.word(),
            "isAVA": random.choice(['Yes', 'No'])
        }
        data.append(record)
    return data
