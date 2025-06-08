


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        record = {
            "Shop_ID": i + 1,
            "Shop_Details": fake.company()  # VARCHAR(255) 타입에 맞는 Faker 메서드
        }
        data.append(record)
    return data
