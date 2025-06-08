



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "City": fake.city(),
            "Country": fake.country(),
            "IATA": fake.airport_iata(),
            "ICAO": fake.airport_icao(),
            "name": fake.company()
        }
        data.append(record)
    return data
