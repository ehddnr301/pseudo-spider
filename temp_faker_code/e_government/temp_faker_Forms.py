



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "form_id": _ + 1,
            "form_type_code": fake.word()[:15],
            "service_id": random.randint(1, 100),
            "form_number": fake.uuid4()[:50],
            "form_name": fake.sentence(nb_words=3)[:80],
            "form_description": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
