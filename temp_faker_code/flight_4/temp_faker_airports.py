



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "apid": _ + 1,
            "name": fake.company(),
            "city": fake.city(),
            "country": fake.country(),
            "x": round(random.uniform(-180, 180), 6),
            "y": round(random.uniform(-90, 90), 6),
            "elevation": random.randint(0, 5000),
            "iata": fake.unique.lexify(text='???'),
            "icao": fake.unique.lexify(text='????')
        }
        data.append(record)
    return data
