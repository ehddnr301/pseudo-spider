



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Party_ID": _ + 1,
            "Year": random.uniform(2000, 2023),
            "Party": fake.word(),
            "Governor": fake.name(),
            "Lieutenant_Governor": fake.name(),
            "Comptroller": fake.name(),
            "Attorney_General": fake.name(),
            "US_Senate": fake.name()
        }
        data.append(record)
    return data
