


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        record = {
            "i_id": i + 1,
            "title": fake.word()[:20]  # varchar(20) 제한에 맞춰서 단어의 길이를 조정
        }
        data.append(record)
    return data
