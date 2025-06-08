


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Company_name": fake.company(),
            "Type": fake.word(),
            "Incorporated_in": fake.date_time_this_year().strftime("%Y-%m-%d"),
            "Group_Equity_Shareholding": round(random.uniform(0, 100), 2),
            "book_club_id": fake.uuid4(),
            "movie_id": fake.uuid4()
        }
        data.append(record)
    return data
