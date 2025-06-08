


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        candidate = {
            "candidate_id": i + 1,
            "candidate_details": fake.sentence(nb_words=10)
        }
        data.append(candidate)
    return data
