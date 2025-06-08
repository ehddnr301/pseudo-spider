



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "user_id": random.randint(1, 1000),
            "role_code": fake.word()[:15],
            "user_name": fake.name(),
            "user_login": fake.user_name(),
            "password": fake.password()
        }
        data.append(record)
    return data
