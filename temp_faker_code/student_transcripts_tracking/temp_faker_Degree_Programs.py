



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "degree_program_id": _ + 1,
            "department_id": random.randint(1, 100),
            "degree_summary_name": fake.catch_phrase(),
            "degree_summary_description": fake.sentence(),
            "other_details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
