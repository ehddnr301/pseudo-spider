


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "network_name": fake.company(),
            "services": fake.bs(),
            "local_authority": fake.city()
        }
        data.append(record)
    return data
