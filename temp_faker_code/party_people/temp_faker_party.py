



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Party_ID": random.randint(1, 1000),
            "Minister": fake.name(),
            "Took_office": fake.date_time_this_year().isoformat(),
            "Left_office": fake.date_time_this_year().isoformat(),
            "Region_ID": random.randint(1, 50),
            "Party_name": fake.word()
        }
        data.append(record)
    return data
