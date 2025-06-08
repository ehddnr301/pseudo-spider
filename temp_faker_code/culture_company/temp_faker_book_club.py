



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "book_club_id": _ + 1,
            "Year": fake.year(),
            "Author_or_Editor": fake.name(),
            "Book_Title": fake.sentence(nb_words=4),
            "Publisher": fake.company(),
            "Category": random.choice(['Fiction', 'Non-Fiction', 'Science', 'History', 'Fantasy']),
            "Result": random.choice(['Read', 'Not Read'])
        }
        data.append(record)
    return data
