



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Election_ID": _ + 1,
            "Representative_ID": random.randint(1, 100),
            "Date": fake.date_time_this_year().isoformat(),
            "Votes": round(random.uniform(1000, 10000), 2),
            "Vote_Percent": round(random.uniform(0, 100), 2),
            "Seats": round(random.uniform(1, 10), 2),
            "Place": round(random.uniform(1, 100), 2)
        }
        data.append(record)
    return data
