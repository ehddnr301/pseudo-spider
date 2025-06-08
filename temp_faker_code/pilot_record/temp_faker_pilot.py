



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Pilot_ID": _ + 1,
            "Pilot_name": fake.name(),
            "Rank": random.randint(1, 10),
            "Age": random.randint(20, 60),
            "Nationality": fake.country(),
            "Position": fake.job(),
            "Join_Year": fake.date_time_this_year().year,
            "Team": fake.company()
        }
        data.append(record)
    return data
