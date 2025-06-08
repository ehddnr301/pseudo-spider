



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "dormid": fake.random_int(min=1, max=1000),
            "dorm_name": fake.word()[:20],
            "student_capacity": fake.random_int(min=1, max=500),
            "gender": random.choice(['M', 'F'])
        }
        data.append(record)
    return data
