



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "player_id": fake.uuid4(),
            "yearid": fake.year(),
            "votedby": fake.random_element(elements=("BBWA", "GIB", "HOF")),
            "ballots": random.randint(1, 100),
            "needed": random.randint(1, 100),
            "votes": random.randint(1, 100),
            "inducted": fake.random_element(elements=("Y", "N")),
            "category": fake.random_element(elements=("Player", "Veteran", "Executive")),
            "needed_note": fake.sentence()
        }
        data.append(record)
    return data
