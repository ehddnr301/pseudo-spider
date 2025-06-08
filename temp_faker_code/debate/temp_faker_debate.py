



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Debate_ID": _ + 1,
            "Date": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            "Venue": fake.city(),
            "Num_of_Audience": random.randint(50, 500)
        }
        data.append(record)
    return data
