


from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    for _ in range(num_records):
        record = {
            "concert_ID": random.randint(1, 1000),
            "Singer_ID": fake.uuid4()
        }
        data.append(record)
    return data
