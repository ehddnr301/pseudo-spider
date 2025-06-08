



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "catalog_id": _ + 1,
            "catalog_name": fake.word()[:50],
            "catalog_publisher": fake.company()[:80],
            "date_of_publication": fake.date_time_this_year(),
            "date_of_latest_revision": fake.date_time_this_year()
        }
        data.append(record)
    return data
