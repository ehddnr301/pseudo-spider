


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "role_code": fake.lexify(text='?????'),  # 5자리의 랜덤 문자열
            "role_description": fake.sentence(nb_words=10)  # 10단어로 이루어진 문장
        }
        data.append(record)
    return data
