



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "year": fake.date_time_this_year().year,
            "team_id": fake.word(),
            "league_id": fake.word(),
            "player_id": fake.uuid4(),
            "g_all": random.uniform(0, 162),
            "gs": random.uniform(0, 162),
            "g_batting": random.randint(0, 162),
            "g_defense": random.uniform(0, 162),
            "g_p": random.randint(0, 162),
            "g_c": random.randint(0, 162),
            "g_1b": random.randint(0, 162),
            "g_2b": random.randint(0, 162),
            "g_3b": random.randint(0, 162),
            "g_ss": random.randint(0, 162),
            "g_lf": random.randint(0, 162),
            "g_cf": random.randint(0, 162),
            "g_rf": random.randint(0, 162),
            "g
