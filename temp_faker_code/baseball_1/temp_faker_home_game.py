



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "year": fake.year(),
            "league_id": fake.word(),
            "team_id": fake.word(),
            "park_id": fake.word(),
            "span_first": fake.date_time_this_year().isoformat(),
            "span_last": fake.date_time_this_year().isoformat(),
            "games": random.randint(1, 162),
            "openings": random.randint(1, 162),
            "attendance": random.randint(1000, 50000)
        }
        data.append(record)
    return data
