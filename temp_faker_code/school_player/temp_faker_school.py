



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "School_ID": _ + 1,
            "School": fake.company(),
            "Location": fake.city(),
            "Enrollment": random.uniform(100, 1000),
            "Founded": fake.date_time_this_year().timestamp(),
            "Denomination": fake.word(),
            "Boys_or_Girls": random.choice(["Boys", "Girls", "Co-Ed"]),
            "Day_or_Boarding": random.choice(["Day", "Boarding"]),
            "Year_Entered_Competition": random.uniform(2000, 2023),
            "School_Colors": fake.color_name()
        }
        data.append(record)
    return data
