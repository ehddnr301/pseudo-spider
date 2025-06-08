



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "AId": _ + 1,
            "Title": fake.sentence(nb_words=3),
            "Year": random.randint(2000, 2023),
            "Label": fake.company(),
            "Type": random.choice(['Album', 'Single', 'EP'])
        }
        data.append(record)
    return data
