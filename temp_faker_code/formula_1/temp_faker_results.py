



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "resultId": _ + 1,
            "raceId": random.randint(1, 100),
            "driverId": random.randint(1, 100),
            "constructorId": random.randint(1, 100),
            "number": random.randint(1, 20),
            "grid": random.randint(1, 20),
            "position": str(random.randint(1, 20)),
            "positionText": fake.word(),
            "positionOrder": random.randint(1, 20),
            "points": round(random.uniform(0, 25), 1),
            "laps": str(random.randint(1, 100)),
            "time": fake.date_time_this_year().strftime("%H:%M:%S"),
            "milliseconds": str(random.randint(100000, 300000)),
            "fastestLap": str(random.randint(1, 100)),
            "rank": str(random.randint(1, 20)),
            "fastestLapTime": fake.date_time_this_year().strftime("%H:%M:%S
