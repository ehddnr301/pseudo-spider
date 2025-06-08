



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "name": fake.city(),
            "lat": round(random.uniform(-90, 90), 6),
            "long": round(random.uniform(-180, 180), 6),
            "dock_count": random.randint(1, 100),
            "city": fake.city(),
            "installation_date": fake.date_time_this_year().isoformat()
        }
        data.append(record)
    return data
