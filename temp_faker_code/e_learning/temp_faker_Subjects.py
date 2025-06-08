


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "subject_id": random.randint(1, 1000),
            "subject_name": fake.word()  # VARCHAR(120) 타입에 맞는 Faker 메서드
        }
        data.append(record)
    return data
