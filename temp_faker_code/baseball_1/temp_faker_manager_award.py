



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
            "league_id": fake.random_element(elements=("AL", "NL")),
            "tie": fake.random_element(elements=("Yes", "No")),
            "notes": random.uniform(0, 100)
        })
    return data
