



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "camera_lens_id": random.randint(1, 100),
            "mountain_id": random.randint(1, 100),
            "color": fake.color_name(),
            "name": fake.word()
        }
        data.append(record)
    return data
