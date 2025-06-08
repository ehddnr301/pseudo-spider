


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Candidate_ID": _ + 1,
            "People_ID": random.randint(1, 100),
            "Poll_Source": fake.company(),
            "Date": fake.date_time_this_year().isoformat(),
            "Support_rate": round(random.uniform(0, 1), 2),
            "Consider_rate": round(random.uniform(0, 1), 2),
            "Oppose_rate": round(random.uniform(0, 1), 2),
            "Unsure_rate": round(random.uniform(0, 1), 2)
        }
        data.append(record)
    return data
