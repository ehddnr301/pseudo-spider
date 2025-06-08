



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Elimination_ID": fake.uuid4(),
            "Wrestler_ID": fake.uuid4(),
            "Team": fake.word(),
            "Eliminated_By": fake.name(),
            "Elimination_Move": fake.word(),
            "Time": fake.date_time_this_year().isoformat()
        }
        data.append(record)
    return data
