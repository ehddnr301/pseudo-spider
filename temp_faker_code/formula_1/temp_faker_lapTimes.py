


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "raceId": fake.random_int(min=1, max=100),
            "driverId": fake.random_int(min=1, max=100),
            "lap": fake.random_int(min=1, max=100),
            "position": fake.random_int(min=1, max=20),
            "time": str(fake.time()),
            "milliseconds": fake.random_int(min=1000, max=300000)
        }
        data.append(record)
    return data
