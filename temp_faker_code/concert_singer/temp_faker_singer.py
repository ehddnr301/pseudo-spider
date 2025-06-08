



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Singer_ID": _ + 1,
            "Name": fake.name(),
            "Country": fake.country(),
            "Song_Name": fake.sentence(nb_words=3),
            "Song_release_year": str(fake.date_time_this_year().year),
            "Age": random.randint(18, 65),
            "Is_male": random.choice([True, False])
        }
        data.append(record)
    return data
