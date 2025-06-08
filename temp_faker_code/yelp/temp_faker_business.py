



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "bid": _ + 1,
            "business_id": fake.uuid4(),
            "name": fake.company(),
            "full_address": fake.address().replace("\n", ", "),
            "city": fake.city(),
            "latitude": str(fake.latitude()),
            "longitude": str(fake.longitude()),
            "review_count": random.randint(0, 1000),
            "is_open": random.randint(0, 1),
            "rating": round(random.uniform(1, 5), 1),
            "state": fake.state()
        }
        data.append(record)
    return data
