



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "team_api_id": random.randint(1, 1000),
            "team_fifa_api_id": random.randint(1, 1000),
            "team_long_name": fake.company() + " FC",
            "team_short_name": fake.word().upper()
        }
        data.append(record)
    return data
