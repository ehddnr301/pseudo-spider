



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "COUNTRY_ID": fake.unique.country_code(),
            "COUNTRY_NAME": fake.country(),
            "REGION_ID": random.randint(1, 10)  # Assuming region IDs are between 1 and 10
        }
        data.append(record)
    return data
