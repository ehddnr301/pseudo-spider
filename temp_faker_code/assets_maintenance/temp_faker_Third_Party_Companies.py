


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "company_id": _ + 1,
            "company_type": random.choice(['LLC', 'Corp', 'Sole', 'Part']),
            "company_name": fake.company(),
            "company_address": fake.address().replace("\n", ", "),
            "other_company_details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
