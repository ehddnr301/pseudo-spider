


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "authorId": random.randint(1, 1000),
            "authorName": fake.name()[:50]  # varchar(50) 제한에 맞춤
        }
        data.append(record)
    return data
