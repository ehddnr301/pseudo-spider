


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        contestant = {
            "contestant_number": i + 1,
            "contestant_name": fake.name()[:50]  # varchar(50) 제한에 맞춤
        }
        data.append(contestant)
    return data
