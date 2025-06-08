



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "constructorStandingsId": _ + 1,
            "raceId": random.randint(1, 100),
            "constructorId": random.randint(1, 100),
            "points": round(random.uniform(0, 100), 2),
            "position": random.randint(1, 20),
            "positionText": fake.word(),
            "wins": random.randint(0, 10)
        }
        data.append(record)
    
    return data
