



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Submission_ID": _ + 1,
            "Scores": round(random.uniform(0, 100), 2),
            "Author": fake.name(),
            "College": fake.company()
        }
        data.append(record)
    return data
