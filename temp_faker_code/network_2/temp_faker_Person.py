


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "name": fake.first_name() + " " + fake.last_name(),
            "age": random.randint(18, 65),
            "city": fake.city(),
            "gender": random.choice(["Male", "Female"]),
            "job": fake.job()
        }
        data.append(record)
    return data
