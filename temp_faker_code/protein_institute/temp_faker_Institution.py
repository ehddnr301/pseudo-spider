



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Institution_id": fake.uuid4(),
            "Institution": fake.company(),
            "Location": fake.city(),
            "Founded": fake.date_time_this_year().timestamp(),
            "Type": random.choice(["Public", "Private", "Non-Profit"]),
            "Enrollment": random.randint(100, 5000),
            "Team": fake.word(),
            "Primary_Conference": random.choice(["Conference A", "Conference B", "Conference C"]),
            "building_id": fake.uuid4()
        }
        data.append(record)
    return data
