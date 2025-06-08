



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Ship_ID": _ + 1,
            "Name": fake.name(),
            "Type": random.choice(["Cargo", "Tanker", "Container", "Ferry", "Cruise"]),
            "Built_Year": fake.date_time_this_year().year,
            "Class": random.choice(["A", "B", "C", "D"]),
            "Flag": fake.country()
        }
        data.append(record)
    return data
