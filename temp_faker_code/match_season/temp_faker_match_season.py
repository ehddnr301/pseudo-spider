



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Season": fake.random_number(digits=4),
            "Player": fake.name(),
            "Position": fake.random_element(elements=("Forward", "Midfielder", "Defender", "Goalkeeper")),
            "Country": fake.random_int(min=1, max=200),
            "Team": fake.random_int(min=1, max=30),
            "Draft_Pick_Number": fake.random_int(min=1, max=100),
            "Draft_Class": fake.word(),
            "College": fake.company()
        }
        data.append(record)
    return data
