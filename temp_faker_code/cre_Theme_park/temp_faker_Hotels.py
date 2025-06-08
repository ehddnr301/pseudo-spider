


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        hotel = {
            "hotel_id": _ + 1,
            "star_rating_code": fake.random_element(elements=('1 Star', '2 Star', '3 Star', '4 Star', '5 Star')),
            "pets_allowed_yn": fake.random_element(elements=('Y', 'N')),
            "price_range": round(random.uniform(50.0, 500.0), 2),
            "other_hotel_details": fake.sentence(nb_words=10)
        }
        data.append(hotel)
    return data
