



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        film_id = random.randint(1, 1000)
        title = fake.sentence(nb_words=6)
        description = fake.text(max_nb_chars=200)
        
        data.append({
            "film_id": film_id,
            "title": title,
            "description": description
        })
    return data
