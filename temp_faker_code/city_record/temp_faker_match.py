


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        match = {
            "Match_ID": _ + 1,
            "Date": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            "Venue": fake.city(),
            "Score": f"{random.randint(0, 5)} - {random.randint(0, 5)}",
            "Result": random.choice(["Win", "Lose", "Draw"]),
            "Competition": fake.word()
        }
        data.append(match)
    return data
