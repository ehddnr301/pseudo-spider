


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "shipping_agent_code": fake.bothify(text='??##########'),  # CHAR(15)
            "shipping_agent_name": fake.company(),  # VARCHAR(255)
            "shipping_agent_description": fake.catch_phrase()  # VARCHAR(255)
        }
        data.append(record)
    return data
