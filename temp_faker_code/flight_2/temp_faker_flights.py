


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Airline": random.randint(1, 100),
            "FlightNo": random.randint(1000, 9999),
            "SourceAirport": fake.city(),
            "DestAirport": fake.city()
        }
        data.append(record)
    return data
