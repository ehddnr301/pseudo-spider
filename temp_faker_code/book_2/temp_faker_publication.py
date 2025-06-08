



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Publication_ID": _ + 1,
            "Book_ID": random.randint(1, 100),
            "Publisher": fake.company(),
            "Publication_Date": fake.date_time_this_year().strftime("%Y-%m-%d"),
            "Price": round(random.uniform(5.0, 100.0), 2)
        }
        data.append(record)
    return data
