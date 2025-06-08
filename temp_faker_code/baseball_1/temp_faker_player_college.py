



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "player_id": fake.uuid4(),
            "college_id": fake.uuid4(),
            "year": random.randint(2000, 2023)
        }
        data.append(record)
    return data
