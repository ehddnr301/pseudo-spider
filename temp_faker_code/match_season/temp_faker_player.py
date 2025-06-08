



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Player_ID": _ + 1,
            "Player": fake.name(),
            "Years_Played": str(random.randint(1, 20)),
            "Total_WL": str(random.randint(0, 100)),
            "Singles_WL": str(random.randint(0, 100)),
            "Doubles_WL": str(random.randint(0, 100)),
            "Team": random.randint(1, 10)
        }
        data.append(record)
    return data
