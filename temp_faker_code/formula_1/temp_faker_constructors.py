



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "constructorId": random.randint(1, 1000),
            "constructorRef": fake.word(),
            "name": fake.company(),
            "nationality": fake.country(),
            "url": fake.url()
        }
        data.append(record)
    return data
