


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "JOB_ID": fake.lexify(text='??????'),  # JOB_ID는 6자리의 랜덤한 문자
            "JOB_TITLE": fake.job(),  # JOB_TITLE은 직업명
            "MIN_SALARY": random.randint(30000, 60000),  # MIN_SALARY는 30000에서 60000 사이의 랜덤한 정수
            "MAX_SALARY": random.randint(60001, 100000)  # MAX_SALARY는 60001에서 100000 사이의 랜덤한 정수
        }
        data.append(record)
    return data
