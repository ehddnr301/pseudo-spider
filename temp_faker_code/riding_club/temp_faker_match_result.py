



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Rank": _ + 1,
            "Club_ID": random.randint(1, 100),
            "Gold": random.randint(0, 10),
            "Big_Silver": random.randint(0, 10),
            "Small_Silver": random.randint(0, 10),
            "Bronze": random.randint(0, 10),
            "Points": random.randint(0, 100)
        }
        data.append(record)
    return data
