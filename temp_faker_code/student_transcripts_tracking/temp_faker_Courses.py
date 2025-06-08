



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "course_id": random.randint(1, 1000),
            "course_name": fake.catch_phrase(),
            "course_description": fake.sentence(),
            "other_details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
