



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Physician": fake.random_int(min=1, max=1000),
            "Department": fake.random_int(min=1, max=100),
            "PrimaryAffiliation": fake.boolean()
        }
        data.append(record)
    return data
