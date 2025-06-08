



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "name": fake.word(),
            "City": fake.city(),
            "Height": random.randint(50, 300),
            "Stories": random.randint(1, 100),
            "Status": random.choice(["Completed", "Under Construction", "Planned"])
        }
        data.append(record)
    return data
