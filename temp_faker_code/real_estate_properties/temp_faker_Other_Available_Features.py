



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "feature_id": _ + 1,
            "feature_type_code": fake.word(),
            "feature_name": fake.word(),
            "feature_description": fake.sentence()
        }
        data.append(record)
    return data
