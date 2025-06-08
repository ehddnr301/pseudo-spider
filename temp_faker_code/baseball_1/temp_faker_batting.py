



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
            "g": random.randint(1, 162),
            "ab": random.randint(1, 600),
            "r": random.randint(0, 200),
            "h": random.randint(0, 300),
            "double": random.randint(0, 50),
            "triple": random.randint(0, 20),
            "hr": random.randint(0, 50),
            "rbi": random.randint(0, 150),
            "sb": random.randint(0, 50),
            "cs": random.randint(0, 20),
            "bb": random.randint(0, 100),
            "so": random.randint(0, 200),
            "ibb": random.randint(0, 20),
            "hbp": random.randint(0, 20),
