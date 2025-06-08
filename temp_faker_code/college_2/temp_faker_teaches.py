



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "ID": fake.bothify(text='??###'),
            "course_id": fake.bothify(text='???###'),
            "sec_id": fake.bothify(text='??###'),
            "semester": random.choice(['Fall', 'Spring', 'Summer']),
            "year": fake.year()
        }
        data.append(record)
    return data
