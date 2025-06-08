



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "architect_id": random.randint(1, 100),
            "id": _ + 1,
            "location": fake.city(),
            "name": fake.company(),
            "type": random.choice(["Factory", "Mill", "Plant"]),
            "built_year": fake.date_time_this_year().year,
            "notes": fake.text(max_nb_chars=200)
        }
        data.append(record)
    return data
