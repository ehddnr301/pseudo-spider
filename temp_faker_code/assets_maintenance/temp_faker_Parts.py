



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "part_id": fake.random_int(min=1, max=1000),
            "part_name": fake.word(),
            "chargeable_yn": random.choice(['Y', 'N']),
            "chargeable_amount": fake.random_number(digits=5),
            "other_part_details": fake.sentence()
        }
        data.append(record)
    return data
