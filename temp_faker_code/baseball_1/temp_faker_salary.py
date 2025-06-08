



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
            "salary": random.randint(30000, 300000)
        }
        data.append(record)
    return data
