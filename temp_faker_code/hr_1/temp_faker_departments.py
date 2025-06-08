



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "DEPARTMENT_ID": random.randint(1, 9999),
            "DEPARTMENT_NAME": fake.word()[:30],
            "MANAGER_ID": random.randint(1, 999999),
            "LOCATION_ID": random.randint(1, 9999)
        }
        data.append(record)
    return data
