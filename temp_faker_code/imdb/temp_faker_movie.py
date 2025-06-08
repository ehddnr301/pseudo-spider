



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        mid = _
        title = fake.sentence(nb_words=3)
        release_year = random.randint(1900, 2023)
        title_aka = fake.sentence(nb_words=3)
        budget = f"${random.randint(1000, 1000000):,}"
        
        data.append({
            "mid": mid,
            "title": title,
            "release_year": release_year,
            "title_aka": title_aka,
            "budget": budget
        })
    return data
