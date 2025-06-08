


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "person_id": _ + 1,
            "first_name": fake.first_name(),
            "middle_name": fake.first_name(),
            "last_name": fake.last_name(),
            "cell_mobile_number": fake.phone_number(),
            "email_address": fake.email(),
            "login_name": fake.user_name(),
            "password": fake.password()
        }
        data.append(record)
    return data
