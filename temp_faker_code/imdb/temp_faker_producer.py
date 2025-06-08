



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "pid": fake.random_int(min=1, max=1000),
            "gender": random.choice(['Male', 'Female']),
            "name": fake.name(),
            "nationality": fake.country(),
            "birth_city": fake.city(),
            "birth_year": fake.year()
        }
        data.append(record)
    return data
