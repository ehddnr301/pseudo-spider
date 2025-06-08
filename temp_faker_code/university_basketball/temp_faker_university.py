



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "School_ID": _ + 1,
            "School": fake.company(),
            "Location": fake.city(),
            "Founded": fake.date_time_this_year().year,
            "Affiliation": fake.company_suffix(),
            "Enrollment": random.uniform(1000, 50000),
            "Nickname": fake.word(),
            "Primary_conference": fake.word()
        }
        data.append(record)
    return data
