



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "year": fake.year(),
            "league_id": fake.word(),
            "team_id": fake.word(),
            "half": random.randint(1, 2),
            "div_id": fake.word(),
            "div_win": fake.word(),
            "rank": random.randint(1, 30),
            "g": random.randint(1, 162),
            "w": random.randint(0, 162),
            "l": random.randint(0, 162)
        }
        data.append(record)
    return data
