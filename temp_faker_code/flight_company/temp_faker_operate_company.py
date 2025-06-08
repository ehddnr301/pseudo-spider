



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "name": fake.company(),
            "Type": random.choice(['Private', 'Public']),
            "Principal_activities": fake.bs(),
            "Incorporated_in": fake.city(),
            "Group_Equity_Shareholding": round(random.uniform(0, 100), 2)
        }
        data.append(record)
    return data
