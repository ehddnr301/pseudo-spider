



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": random.uniform(1, 1000),
            "Episode": fake.sentence(nb_words=3),
            "Air_Date": fake.date_time_this_year().strftime("%Y-%m-%d"),
            "Rating": str(random.uniform(1, 10)),
            "Share": random.uniform(0, 1),
            "18_49_Rating_Share": str(random.uniform(0, 1)),
            "Viewers_m": str(random.randint(1, 100)),
            "Weekly_Rank": random.uniform(1, 100),
            "Channel": fake.word()
        }
        data.append(record)
    return data
