



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "DNO": random.randint(1, 100),
            "Division": fake.random_letter().upper() + fake.random_letter().upper(),
            "DName": fake.company(),
            "Room": fake.random_int(min=1, max=9999),
            "Building": fake.word() + " Building",
            "DPhone": fake.random_int(min=1000000000, max=9999999999)
        }
        data.append(record)
    return data
