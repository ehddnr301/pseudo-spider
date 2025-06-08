


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "task_id": _ + 1,
            "project_id": random.randint(1, 100),
            "task_details": fake.sentence(nb_words=10),
            "eg Agree Objectives": random.choice(['Y', 'N'])
        }
        data.append(record)
    return data
