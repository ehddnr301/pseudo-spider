


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "property_type_code": fake.lexify(text='?????'),  # 5자리의 랜덤 문자열
            "property_type_description": fake.sentence(nb_words=6)  # 6단어로 구성된 문장
        }
        data.append(record)
    return data
