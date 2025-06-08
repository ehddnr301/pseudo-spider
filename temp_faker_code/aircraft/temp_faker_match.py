



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Round": random.uniform(1, 100),
            "Location": fake.city(),
            "Country": fake.country(),
            "Date": fake.date_time_this_year().isoformat(),
            "Fastest_Qualifying": fake.name(),
            "Winning_Pilot": fake.name(),
            "Winning_Aircraft": fake.word()
        }
        data.append(record)
    return data
