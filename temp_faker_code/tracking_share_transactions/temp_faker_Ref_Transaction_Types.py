


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "transaction_type_code": fake.lexify(text='??????'),  # 6자리의 랜덤 문자열
            "transaction_type_description": fake.sentence(nb_words=10)  # 10단어로 이루어진 문장
        }
        data.append(record)
    return data
