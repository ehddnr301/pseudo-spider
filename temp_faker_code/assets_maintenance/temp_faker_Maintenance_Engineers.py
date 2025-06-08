


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "engineer_id": _ + 1,
            "company_id": random.randint(1, 100),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "other_details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
