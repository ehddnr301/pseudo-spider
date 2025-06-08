



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Estimation_ID": _ + 1,
            "Low_Estimate": round(random.uniform(1000, 50000), 2),
            "High_Estimate": round(random.uniform(50000, 200000), 2),
            "Film_ID": random.randint(1, 100),
            "Type": fake.word(),
            "Market_ID": random.randint(1, 10),
            "Year": fake.date_time_this_year().year
        }
        data.append(record)
    return data
