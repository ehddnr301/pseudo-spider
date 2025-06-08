


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        record = {
            "keyphraseId": i + 1,
            "keyphraseName": fake.word()[:50]  # varchar(50) 타입에 맞게 50자 이하로 생성
        }
        data.append(record)
    return data
