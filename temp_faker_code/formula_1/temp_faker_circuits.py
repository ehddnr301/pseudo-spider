



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "circuitId": _ + 1,
            "circuitRef": fake.word(),
            "name": fake.company(),
            "location": fake.city(),
            "country": fake.country(),
            "lat": round(random.uniform(-90, 90), 6),
            "lng": round(random.uniform(-180, 180), 6),
            "alt": str(random.randint(0, 5000)),
            "url": fake.url()
        }
        data.append(record)
    return data
