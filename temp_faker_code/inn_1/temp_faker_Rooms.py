



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "RoomId": fake.uuid4(),
            "roomName": fake.word(),
            "beds": random.randint(1, 5),
            "bedType": random.choice(["Single", "Double", "Queen", "King"]),
            "maxOccupancy": random.randint(1, 4),
            "basePrice": random.randint(50, 500),
            "decor": fake.word()
        }
        data.append(record)
    return data
