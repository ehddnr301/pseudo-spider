


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "feature_type_code": fake.lexify(text='??????'),  # 6자리 랜덤 문자열
            "feature_type_name": fake.catch_phrase()  # 랜덤 문구
        }
        data.append(record)
    return data
