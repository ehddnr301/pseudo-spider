


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "course_id": random.randint(1, 1000),
            "author_id": random.randint(1, 100),
            "subject_id": random.randint(1, 50),
            "course_name": fake.sentence(nb_words=3),
            "course_description": fake.text(max_nb_chars=200)
        }
        data.append(record)
    return data
