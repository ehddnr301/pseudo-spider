


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "breed_code": fake.lexify(text='??????'),  # 6자리의 랜덤한 문자
            "breed_name": fake.word()  # 단어 생성
        }
        data.append(record)
    return data
