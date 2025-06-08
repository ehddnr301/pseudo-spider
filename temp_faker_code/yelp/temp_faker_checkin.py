



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "cid": _ + 1,
            "business_id": fake.uuid4(),
            "count": random.randint(1, 100),
            "day": fake.date_time_this_year().strftime("%A")
        }
        data.append(record)
    return data
