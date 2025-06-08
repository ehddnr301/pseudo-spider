



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Track_ID": _ + 1,
            "Name": fake.name(),
            "Location": fake.city(),
            "Seating": round(random.uniform(1000, 50000), 2),
            "Year_Opened": fake.date_time_this_year().year
        }
        data.append(record)
    return data
