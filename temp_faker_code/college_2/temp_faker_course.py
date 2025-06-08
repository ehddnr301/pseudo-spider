



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "course_id": fake.bothify(text='??###???'),
            "title": fake.catch_phrase(),
            "dept_name": fake.word()[:20],
            "credits": random.randint(1, 4)
        }
        data.append(record)
    return data
