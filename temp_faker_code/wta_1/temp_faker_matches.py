



from faker import Faker
import random
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "best_of": random.choice([3, 5]),
            "draw_size": random.randint(16, 128),
            "loser_age": round(random.uniform(18, 40), 1),
            "loser_entry": fake.word(),
            "loser_hand": random.choice(['L', 'R']),
            "loser_ht": random.randint(160, 210),
            "loser_id": random.randint(1, 1000),
            "loser_ioc": fake.country_code(),
            "loser_name": fake.name(),
            "loser_rank": random.randint(1, 100),
            "loser_rank_points": random.randint(0, 5000),
            "loser_seed": random.randint(1, 32),
            "match_num": random.randint(1, 100),
            "minutes": random.randint(30, 300),
            "round": random.choice(['1st', '2nd', 'Quarterfinal', 'Semifinal', 'Final']),
