



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "alid": _ + 1,
            "name": fake.company(),
            "iata": fake.random_uppercase_letter() + fake.random_uppercase_letter(),
            "icao": fake.random_uppercase_letter() + fake.random_uppercase_letter() + fake.random_uppercase_letter(),
            "callsign": fake.word(),
            "country": fake.country(),
            "active": random.choice(['Y', 'N'])
        }
        data.append(record)
    return data
