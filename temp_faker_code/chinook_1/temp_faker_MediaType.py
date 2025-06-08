


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "MediaTypeId": _ + 1,
            "Name": fake.word()  # varchar(120) 타입에 맞는 Faker 메서드
        }
        data.append(record)
    return data
