



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Department_ID": _ + 1,
            "Name": fake.word(),
            "Creation": fake.date_time_this_year().isoformat(),
            "Ranking": random.randint(1, 10),
            "Budget_in_Billions": round(random.uniform(1, 100), 2),
            "Num_Employees": round(random.uniform(1, 10000), 2)
        }
        data.append(record)
    return data
