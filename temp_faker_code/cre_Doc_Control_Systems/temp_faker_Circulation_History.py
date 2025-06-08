



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "document_id": fake.random_int(min=1, max=1000),
            "draft_number": fake.random_int(min=1, max=100),
            "copy_number": fake.random_int(min=1, max=10),
            "employee_id": fake.random_int(min=1, max=500)
        }
        data.append(record)
    return data
