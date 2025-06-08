


from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "StuID": fake.random_int(min=1, max=1000),
            "SportName": fake.word()[:32],
            "HoursPerWeek": fake.random_int(min=1, max=40),
            "GamesPlayed": fake.random_int(min=0, max=100),
            "OnScholarship": random.choice(['Y', 'N'])
        }
        data.append(record)
    return data
