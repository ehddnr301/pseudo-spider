



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        player = {
            "Player_ID": _ + 1,
            "name": fake.name(),
            "Position": random.choice(["Forward", "Midfielder", "Defender", "Goalkeeper"]),
            "Club_ID": random.randint(1, 20),
            "Apps": round(random.uniform(0, 100), 2),
            "Tries": round(random.uniform(0, 50), 2),
            "Goals": str(random.randint(0, 30)),
            "Points": round(random.uniform(0, 200), 2)
        }
        data.append(player)
    return data
