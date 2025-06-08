


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "School_ID": random.randint(1, 1000),
            "Nickname": fake.word(),
            "Colors": fake.color_name(),
            "League": fake.word(),
            "Class": fake.word(),
            "Division": fake.word()
        }
        data.append(record)
    return data
