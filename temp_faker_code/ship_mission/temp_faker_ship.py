



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Ship_ID": _ + 1,
            "Name": fake.company(),
            "Type": random.choice(["Cargo", "Tanker", "Container", "Ferry", "Cruise"]),
            "Nationality": fake.country(),
            "Tonnage": random.randint(1000, 50000)
        }
        data.append(record)
    return data
