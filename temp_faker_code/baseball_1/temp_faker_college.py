


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "college_id": fake.uuid4(),
            "name_full": fake.company(),
            "city": fake.city(),
            "state": fake.state(),
            "country": fake.country()
        }
        data.append(record)
    return data
