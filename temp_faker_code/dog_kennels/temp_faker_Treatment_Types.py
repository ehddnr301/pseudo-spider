


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "treatment_type_code": fake.lexify(text='?????'),  # 5자리의 랜덤한 문자
            "treatment_type_description": fake.sentence(nb_words=6)  # 6단어로 이루어진 문장
        }
        data.append(record)
    return data
