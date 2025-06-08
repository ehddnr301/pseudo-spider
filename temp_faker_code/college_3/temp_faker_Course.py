


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "CID": fake.bothify(text='???-###'),
            "CName": fake.catch_phrase(),
            "Credits": random.randint(1, 5),
            "Instructor": random.randint(1, 100),
            "Days": fake.day_of_week(),
            "Hours": fake.time(),
            "DNO": random.randint(1, 10)
        }
        data.append(record)
    return data
