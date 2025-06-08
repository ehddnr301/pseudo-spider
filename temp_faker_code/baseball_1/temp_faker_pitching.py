



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "player_id": fake.uuid4(),
            "year": fake.year(),
            "stint": random.randint(1, 5),
            "team_id": fake.word(),
            "league_id": fake.word(),
            "w": random.randint(0, 20),
            "l": random.randint(0, 20),
            "g": random.randint(0, 162),
            "gs": random.randint(0, 30),
            "cg": random.randint(0, 10),
            "sho": random.randint(0, 5),
            "sv": random.randint(0, 40),
            "ipouts": random.uniform(0, 1000),
            "h": random.randint(0, 300),
            "er": random.randint(0, 200),
            "hr": random.randint(0, 100),
            "bb": random.randint(0, 100),
            "so": random.randint(0, 300),
            "baopp": random.uniform(0, 1),
