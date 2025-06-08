



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Team_ID": _ + 1,
            "School_ID": random.randint(1, 100),
            "Team_Name": fake.name(),
            "ACC_Regular_Season": fake.word(),
            "ACC_Percent": f"{random.randint(50, 100)}%",
            "ACC_Home": f"{random.randint(1, 20)}-0",
            "ACC_Road": f"{random.randint(1, 20)}-0",
            "All_Games": f"{random.randint(1, 20)}-0",
            "All_Games_Percent": random.randint(50, 100),
            "All_Home": f"{random.randint(1, 20)}-0",
            "All_Road": f"{random.randint(1, 20)}-0",
            "All_Neutral": f"{random.randint(1, 20)}-0"
        }
        data.append(record)
    return data
