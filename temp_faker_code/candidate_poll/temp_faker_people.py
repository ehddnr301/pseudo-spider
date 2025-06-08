



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "People_ID": _ + 1,
            "Sex": random.choice(['Male', 'Female']),
            "Name": fake.name(),
            "Date_of_Birth": fake.date_time_this_year().strftime('%Y-%m-%d'),
            "Height": round(random.uniform(150.0, 200.0), 2),
            "Weight": round(random.uniform(50.0, 100.0), 2)
        }
        data.append(record)
    return data
