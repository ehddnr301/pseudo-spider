



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "player_id": fake.uuid4(),
            "year": fake.year(),
            "stint": random.randint(1, 5),
            "glf": round(random.uniform(0, 1), 3),
            "gcf": round(random.uniform(0, 1), 3),
            "grf": round(random.uniform(0, 1), 3)
        }
        data.append(record)
    return data
