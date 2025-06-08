


from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "document_code": fake.bothify(text='??###'),
            "functional_area_code": fake.bothify(text='??###')
        }
        data.append(record)
    return data
