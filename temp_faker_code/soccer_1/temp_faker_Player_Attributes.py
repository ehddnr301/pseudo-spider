



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "player_fifa_api_id": fake.random_int(min=1, max=100000),
            "player_api_id": fake.random_int(min=1, max=100000),
            "date": fake.date_time_this_year().isoformat(),
            "overall_rating": fake.random_int(min=1, max=100),
            "potential": fake.random_int(min=1, max=100),
            "preferred_foot": fake.random_element(elements=("Left", "Right")),
            "attacking_work_rate": fake.random_element(elements=("Low", "Medium", "High")),
            "defensive_work_rate": fake.random_element(elements=("Low", "Medium", "High")),
            "crossing": fake.random_int(min=1, max=100),
            "finishing": fake.random_int(min=1, max=100),
            "heading_accuracy": fake.random_int(min=1, max=100),
            "short_passing": fake.random_int(min=1, max=100),
            "volleys":
