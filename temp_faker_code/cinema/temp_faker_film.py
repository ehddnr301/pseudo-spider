



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Film_ID": _ + 1,
            "Rank_in_series": random.randint(1, 10),
            "Number_in_season": random.randint(1, 20),
            "Title": fake.catch_phrase(),
            "Directed_by": fake.name(),
            "Original_air_date": fake.date_time_this_year().isoformat(),
            "Production_code": fake.bothify(text='??-###')
        }
        data.append(record)
    return data
