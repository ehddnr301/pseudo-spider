



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "f_id": random.randint(1, 1000000000),
            "artist_name": fake.name(),
            "file_size": f"{random.randint(1, 100)} MB",
            "duration": f"{random.randint(1, 300)} seconds",
            "formats": random.choice(["mp3", "wav", "flac", "aac"])
        }
        data.append(record)
    
    return data
