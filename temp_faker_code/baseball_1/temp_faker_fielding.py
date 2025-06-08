



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
            "pos": fake.random_element(elements=("P", "C", "1B", "2B", "3B", "SS", "OF")),
            "g": random.randint(1, 162),
            "gs": random.uniform(0, 162),
            "inn_outs": random.uniform(0, 500),
            "po": random.uniform(0, 100),
            "a": random.uniform(0, 100),
            "e": random.uniform(0, 100),
            "dp": random.uniform(0, 100),
            "pb": random.uniform(0, 100),
            "wp": random.uniform(0, 100),
            "sb": random.uniform(0, 100),
            "cs": random.uniform(0, 100),
            "zr": random.uniform
