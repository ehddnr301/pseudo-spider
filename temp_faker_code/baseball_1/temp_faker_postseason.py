



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "year": fake.year(),
            "round": fake.word(),
            "team_id_winner": fake.word(),
            "league_id_winner": fake.word(),
            "team_id_loser": fake.word(),
            "league_id_loser": fake.word(),
            "wins": random.randint(0, 10),
            "losses": random.randint(0, 10),
            "ties": random.randint(0, 10)
        }
        data.append(record)
    return data
