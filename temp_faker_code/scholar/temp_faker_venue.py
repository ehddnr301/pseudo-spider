


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "venueId": fake.unique.random_int(min=1, max=1000),
            "venueName": fake.company()  # varchar(100) 타입에 맞는 Faker 메서드
        }
        data.append(record)
    return data
