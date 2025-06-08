



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        record = {
            "building_id": i + 1,
            "building_short_name": fake.word()[:15],
            "building_full_name": fake.sentence(nb_words=6)[:-1],
            "building_description": fake.text(max_nb_chars=255),
            "building_address": fake.address().replace("\n", ", "),
            "building_manager": fake.name(),
            "building_phone": fake.phone_number()
        }
        data.append(record)
    return data
