


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "staff_id": random.randint(1, 1000),
            "staff_first_name": fake.first_name(),
            "staff_last_name": fake.last_name(),
            "other_staff_details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
