



from faker import Faker
import random
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "team_fifa_api_id": random.randint(1, 1000),
            "team_api_id": random.randint(1, 1000),
            "date": fake.date_time_this_year().isoformat(),
            "buildUpPlaySpeed": random.randint(1, 100),
            "buildUpPlaySpeedClass": fake.word(),
            "buildUpPlayDribbling": random.randint(1, 100),
            "buildUpPlayDribblingClass": fake.word(),
            "buildUpPlayPassing": random.randint(1, 100),
            "buildUpPlayPassingClass": fake.word(),
            "buildUpPlayPositioningClass": fake.word(),
            "chanceCreationPassing": random.randint(1, 100),
            "chanceCreationPassingClass": fake.word(),
            "chanceCreationCrossing": random.randint(1, 100),
            "chanceCreationCrossingClass": fake.word(),
            "chanceCreationShooting": random.randint(1, 100
