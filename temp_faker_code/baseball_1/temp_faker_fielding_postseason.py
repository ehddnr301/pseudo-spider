



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "player_id": fake.uuid4(),
            "year": fake.date_time_this_year().year,
            "team_id": fake.word(),
            "league_id": fake.word(),
            "round": fake.word(),
            "pos": fake.word(),
            "g": random.randint(1, 10),
            "gs": random.uniform(0, 10),
            "inn_outs": random.uniform(0, 10),
            "po": random.randint(0, 10),
            "a": random.randint(0, 10),
            "e": random.randint(0, 10),
            "dp": random.randint(0, 10),
            "tp": random.randint(0, 10),
            "pb": random.uniform(0, 10),
            "sb": random.uniform(0, 10),
            "cs": random.uniform(0, 10)
        }
        data.append(record)
    return data
