



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Musical_ID": _ + 1,
            "Name": fake.catch_phrase(),
            "Year": fake.date_time_this_year().year,
            "Award": fake.word(),
            "Category": fake.word(),
            "Nominee": fake.name(),
            "Result": random.choice(["Won", "Nominated", "Lost"])
        }
        data.append(record)
    return data
