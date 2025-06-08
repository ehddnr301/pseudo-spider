



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        year = fake.date_time_this_year().year
        data.append({
            "award_id": fake.uuid4(),
            "year": year,
            "league_id": fake.word(),
            "player_id": fake.uuid4(),
            "points_won": random.randint(1, 100),
            "points_max": random.randint(100, 200),
            "votes_first": random.randint(0, 50)
        })
    return data
