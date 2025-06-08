


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        size_code = fake.unique.lexify(text='??????')  # 6자리의 랜덤한 문자열 생성
        size_description = fake.text(max_nb_chars=80)  # 80자 이하의 랜덤한 ��스트 생성
        data.append({
            "size_code": size_code,
            "size_description": size_description
        })
    return data
