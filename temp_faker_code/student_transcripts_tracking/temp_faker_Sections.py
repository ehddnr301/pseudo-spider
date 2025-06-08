



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    for _ in range(num_records):
        record = {
            "section_id": _ + 1,
            "course_id": random.randint(1, 100),
            "section_name": fake.word(),
            "section_description": fake.sentence(),
            "other_details": fake.sentence()
        }
        data.append(record)
    return data
