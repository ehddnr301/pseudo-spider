



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "player_id": fake.uuid4(),
            "year": fake.year(),
            "game_num": random.randint(1, 10),
            "game_id": fake.uuid4(),
            "team_id": fake.random_element(elements=("team_a", "team_b", "team_c")),
            "league_id": fake.random_element(elements=("league_a", "league_b")),
            "gp": random.uniform(0, 1),
            "starting_pos": random.randint(1, 5)
        }
        data.append(record)
    return data
