



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        year = fake.date_time_this_year().year
        data.append({
            "player_id": fake.uuid4(),
            "award_id": fake.uuid4(),
            "year": year,
            "league_id": fake.word(),
            "tie": fake.word(),
            "notes": fake.sentence()
        })
    return data
