


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Poker_Player_ID": _ + 1,
            "People_ID": random.randint(1, 1000),
            "Final_Table_Made": round(random.uniform(0, 1), 2),
            "Best_Finish": round(random.uniform(0, 1), 2),
            "Money_Rank": round(random.uniform(1, 100), 2),
            "Earnings": round(random.uniform(0, 100000), 2)
        }
        data.append(record)
    return data
