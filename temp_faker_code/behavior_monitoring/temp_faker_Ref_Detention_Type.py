


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "detention_type_code": fake.lexify(text='??????'),  # 6자리의 랜덤 문자열
            "detention_type_description": fake.sentence(nb_words=6)  # 6단어로 이루어진 문장
        }
        data.append(record)
    return data
