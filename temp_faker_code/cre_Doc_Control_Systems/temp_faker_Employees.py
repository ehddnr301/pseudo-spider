


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "employee_id": random.randint(1, 1000),
            "role_code": fake.lexify(text='?????'),
            "employee_name": fake.name(),
            "other_details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
