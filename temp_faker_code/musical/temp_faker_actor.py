



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Actor_ID": _ + 1,
            "Name": fake.name(),
            "Musical_ID": random.randint(1, 100),
            "Character": fake.word(),
            "Duration": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            "age": random.randint(18, 70)
        }
        data.append(record)
    return data
