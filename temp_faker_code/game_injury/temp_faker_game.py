



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "stadium_id": random.randint(1, 100),
            "id": _ + 1,
            "Season": random.randint(1, 10),
            "Date": fake.date_time_this_year().isoformat(),
            "Home_team": fake.company(),
            "Away_team": fake.company(),
            "Score": f"{random.randint(0, 5)} - {random.randint(0, 5)}",
            "Competition": fake.word()
        }
        data.append(record)
    return data
