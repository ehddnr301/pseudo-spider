



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "semester_id": _ + 1,
            "semester_name": fake.word().capitalize(),
            "semester_description": fake.sentence(),
            "other_details": fake.sentence()
        }
        data.append(record)
    
    return data
