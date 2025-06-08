


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "course_id": fake.uuid4(),
            "course_name": fake.catch_phrase(),
            "course_description": fake.text(max_nb_chars=255),
            "other_details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
