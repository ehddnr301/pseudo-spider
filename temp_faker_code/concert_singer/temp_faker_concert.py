



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        concert = {
            "concert_ID": _ + 1,
            "concert_Name": fake.catch_phrase(),
            "Theme": fake.word(),
            "Stadium_ID": fake.uuid4(),
            "Year": str(fake.date_time_this_year().year)
        }
        data.append(concert)
    return data
