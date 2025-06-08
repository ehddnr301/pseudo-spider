



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Member_ID": random.randint(1, 1000),
            "Name": fake.name(),
            "Country": fake.country(),
            "College_ID": random.randint(1, 100)
        }
        data.append(record)
    return data
