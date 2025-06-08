



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Mission_ID": _ + 1,
            "Ship_ID": random.randint(1, 100),
            "Code": fake.word(),
            "Launched_Year": fake.date_time_this_year().year,
            "Location": fake.city(),
            "Speed_knots": random.randint(1, 30),
            "Fate": fake.word()
        }
        data.append(record)
    return data
