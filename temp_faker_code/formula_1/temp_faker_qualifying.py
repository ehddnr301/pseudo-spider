



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "qualifyId": _ + 1,
            "raceId": random.randint(1, 100),
            "driverId": random.randint(1, 100),
            "constructorId": random.randint(1, 100),
            "number": random.randint(1, 20),
            "position": random.randint(1, 20),
            "q1": fake.time(),
            "q2": fake.time(),
            "q3": fake.time()
        }
        data.append(record)
    return data
