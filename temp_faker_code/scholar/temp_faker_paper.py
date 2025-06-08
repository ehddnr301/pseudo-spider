



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        paper = {
            "paperId": _ + 1,
            "title": fake.sentence(nb_words=6),
            "venueId": random.randint(1, 100),
            "year": fake.date_time_this_year().year,
            "numCiting": random.randint(0, 1000),
            "numCitedBy": random.randint(0, 1000),
            "journalId": random.randint(1, 100)
        }
        data.append(paper)
    return data
