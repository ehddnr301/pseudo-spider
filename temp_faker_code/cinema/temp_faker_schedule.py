



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Cinema_ID": random.randint(1, 100),
            "Film_ID": random.randint(1, 100),
            "Date": fake.date_time_this_year().strftime("%Y-%m-%d"),
            "Show_times_per_day": random.randint(1, 10),
            "Price": round(random.uniform(5.0, 15.0), 2)
        }
        data.append(record)
    return data
