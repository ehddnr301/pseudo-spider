



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        year = fake.date_time_this_year().year
        data.append({
            "award_id": fake.word(),
            "year": year,
            "league_id": fake.word(),
            "player_id": fake.uuid4(),
            "points_won": random.uniform(0, 100),
            "points_max": random.randint(1, 100),
            "votes_first": random.uniform(0, 100)
        })
    return data
