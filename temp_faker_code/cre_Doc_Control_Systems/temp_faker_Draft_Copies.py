


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        document_id = fake.random_int(min=1, max=1000)
        draft_number = fake.random_int(min=1, max=100)
        copy_number = fake.random_int(min=1, max=10)
        
        record = {
            "document_id": document_id,
            "draft_number": draft_number,
            "copy_number": copy_number
        }
        data.append(record)
    return data
