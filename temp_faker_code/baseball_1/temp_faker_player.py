



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "player_id": fake.uuid4(),
            "birth_year": fake.year(),
            "birth_month": random.randint(1, 12),
            "birth_day": random.randint(1, 28),
            "birth_country": fake.country(),
            "birth_state": fake.state(),
            "birth_city": fake.city(),
            "death_year": random.choice([None, fake.year()]),
            "death_month": random.choice([None, random.randint(1, 12)]),
            "death_day": random.choice([None, random.randint(1, 28)]),
            "death_country": random.choice([None, fake.country()]),
            "death_state": random.choice([None, fake.state()]),
            "death_city": random.choice([None, fake.city()]),
            "name_first": fake.first_name(),
            "name_last": fake.last_name(),
            "name_given": fake.name(),
            "weight": random.uniform(50, 150),
            "height": random.uniform(150, 200),
            "bats": random
