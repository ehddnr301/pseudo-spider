



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "FacID": _ + 1,
            "Lname": fake.last_name(),
            "Fname": fake.first_name(),
            "Rank": random.choice(["Professor", "Associate Professor", "Assistant Professor"]),
            "Sex": random.choice(["M", "F"]),
            "Phone": fake.phone_number().replace("-", "").replace(" ", ""),
            "Room": fake.random_int(min=100, max=999),
            "Building": fake.word()[:13]
        }
        data.append(record)
    return data
