



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Volume_ID": _ + 1,
            "Volume_Issue": fake.word(),
            "Issue_Date": fake.date_time_this_year().isoformat(),
            "Weeks_on_Top": round(random.uniform(1, 52), 2),
            "Song": fake.sentence(nb_words=3),
            "Artist_ID": random.randint(1, 100)
        }
        data.append(record)
    return data
