



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "City_ID": _ + 1,
            "Jan": round(random.uniform(-10, 30), 2),
            "Feb": round(random.uniform(-10, 30), 2),
            "Mar": round(random.uniform(-10, 30), 2),
            "Apr": round(random.uniform(-10, 30), 2),
            "Jun": round(random.uniform(-10, 30), 2),
            "Jul": round(random.uniform(-10, 30), 2),
            "Aug": round(random.uniform(-10, 30), 2),
            "Sep": round(random.uniform(-10, 30), 2),
            "Oct": round(random.uniform(-10, 30), 2),
            "Nov": round(random.uniform(-10, 30), 2),
            "Dec": round(random.uniform(-10, 30), 2),
        }
        data.append(record)
    return data
