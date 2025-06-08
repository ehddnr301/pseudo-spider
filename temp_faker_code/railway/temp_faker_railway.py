



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Railway_ID": _ + 1,
            "Railway": fake.company(),
            "Builder": fake.company(),
            "Built": fake.date_time_this_year().strftime("%Y-%m-%d"),
            "Wheels": str(random.randint(2, 12)),
            "Location": fake.city(),
            "ObjectNumber": fake.uuid4()
        }
        data.append(record)
    return data
