



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        outcome_code = fake.unique.lexify(text='??????')  # 6자리 랜덤 문자열
        outcome_description = fake.sentence(nb_words=10)  # 10단어로 이루어진 문장
        data.append({
            "outcome_code": outcome_code,
            "outcome_description": outcome_description
        })
    return data
