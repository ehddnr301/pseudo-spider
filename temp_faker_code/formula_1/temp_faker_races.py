



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        race = {
            "raceId": _ + 1,
            "year": fake.year(),
            "round": random.randint(1, 20),
            "circuitId": random.randint(1, 100),
            "name": fake.catch_phrase(),
            "date": fake.date_time_this_year().isoformat(),
            "time": fake.time(),
            "url": fake.url()
        }
        data.append(race)
    return data
