



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "year": fake.year(),
            "round": fake.random_element(elements=("ALDS", "ALCS", "NLDS", "NLCS", "WS")),
            "player_id": fake.uuid4(),
            "team_id": fake.random_element(elements=("BOS", "NYY", "LAD", "CHC", "HOU")),
            "league_id": fake.random_element(elements=("AL", "NL")),
            "g": random.randint(1, 7),
            "ab": random.randint(1, 5),
            "r": random.randint(0, 10),
            "h": random.randint(0, 5),
            "double": random.randint(0, 2),
            "triple": random.randint(0, 1),
            "hr": random.randint(0, 3),
            "rbi": random.randint(0, 5),
            "sb": random.randint(0, 3),
            "cs": random.uniform(0, 1),
            "bb": random.randint(0
