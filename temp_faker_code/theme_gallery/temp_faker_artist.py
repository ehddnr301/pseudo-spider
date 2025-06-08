



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        artist = {
            "Artist_ID": _ + 1,
            "Name": fake.name(),
            "Country": fake.country(),
            "Year_Join": random.randint(2000, 2023),
            "Age": random.randint(18, 65)
        }
        data.append(artist)
    return data
