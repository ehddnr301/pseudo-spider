



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "train_number": random.randint(1000, 9999),
            "name": fake.name(),
            "origin": fake.city(),
            "destination": fake.city(),
            "time": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            "interval": f"{random.randint(5, 60)} minutes"
        }
        data.append(record)
    return data
