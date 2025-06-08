



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        year = fake.date_time_this_year().year
        data.append({
            "No": _ + 1,
            "Grape": fake.word(),
            "Winery": fake.company(),
            "Appelation": fake.city(),
            "State": fake.state(),
            "Name": fake.word(),
            "Year": year,
            "Price": random.randint(10, 100),
            "Score": random.randint(80, 100),
            "Cases": random.randint(1, 100),
            "Drink": fake.word()
        })
    return data
