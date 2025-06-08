



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Event_ID": _ + 1,
            "Date": fake.date_time_this_year().isoformat(),
            "Venue": fake.city(),
            "Name": fake.catch_phrase(),
            "Event_Attendance": random.randint(1, 1000)
        }
        data.append(record)
    return data
