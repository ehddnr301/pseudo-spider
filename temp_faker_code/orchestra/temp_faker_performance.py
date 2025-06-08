


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Performance_ID": _ + 1,
            "Orchestra_ID": random.randint(1, 100),
            "Type": fake.word(),
            "Date": fake.date_time_this_year().isoformat(),
            "Official_ratings_(millions)": round(random.uniform(1, 10), 2),
            "Weekly_rank": str(random.randint(1, 100)),
            "Share": str(random.randint(1, 100)) + '%'
        }
        data.append(record)
    return data
