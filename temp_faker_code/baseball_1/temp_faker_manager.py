



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "player_id": fake.uuid4(),
            "year": fake.year(),
            "team_id": fake.word(),
            "league_id": fake.word(),
            "inseason": random.randint(0, 1),
            "g": random.randint(0, 162),
            "w": random.randint(0, 162),
            "l": random.randint(0, 162),
            "rank": random.uniform(1, 30),
            "plyr_mgr": fake.name()
        }
        data.append(record)
    return data
