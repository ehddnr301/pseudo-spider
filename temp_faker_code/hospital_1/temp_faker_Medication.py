



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Code": random.randint(1, 1000),
            "Name": fake.word()[:30],
            "Brand": fake.word()[:30],
            "Description": fake.sentence()[:30]
        }
        data.append(record)
    return data
