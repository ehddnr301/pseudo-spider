



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "driverStandingsId": _ + 1,
            "raceId": random.randint(1, 100),
            "driverId": random.randint(1, 100),
            "points": round(random.uniform(0, 100), 1),
            "position": random.randint(1, 20),
            "positionText": fake.word(),
            "wins": random.randint(0, 10)
        }
        data.append(record)
    return data
