



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Player_ID": _ + 1,
            "Sponsor_name": fake.company(),
            "Player_name": fake.name(),
            "Gender": random.choice(['Male', 'Female']),
            "Residence": fake.city(),
            "Occupation": fake.job(),
            "Votes": random.randint(0, 100),
            "Rank": random.choice(['A', 'B', 'C', 'D', 'E'])
        }
        data.append(record)
    return data
