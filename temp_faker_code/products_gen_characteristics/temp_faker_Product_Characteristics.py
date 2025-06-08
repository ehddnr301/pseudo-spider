


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "product_id": random.randint(1, 1000),
            "characteristic_id": random.randint(1, 100),
            "product_characteristic_value": fake.word()  # VARCHAR(50) 타입에 맞는 값
        }
        data.append(record)
    return data
