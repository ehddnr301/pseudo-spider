



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": fake.uuid4(),
            "series_name": fake.catch_phrase(),
            "Country": fake.country(),
            "Language": fake.language_name(),
            "Content": fake.text(max_nb_chars=200),
            "Pixel_aspect_ratio_PAR": random.choice(['1:1', '4:3', '16:9', '21:9']),
            "Hight_definition_TV": random.choice(['Yes', 'No']),
            "Pay_per_view_PPV": random.choice(['Yes', 'No']),
            "Package_Option": random.choice(['Basic', 'Standard', 'Premium']),
        }
        data.append(record)
    return data
