#!/usr/bin/env python3

from config import app, db
# from models import MODELS GO HERE
from models import Candy, Country
from faker import Faker
import random

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        # write your seeds here!

        Candy.query.delete()

        #Manual
        c1 = Candy(name="Reese's", brand="Hershey", price=2)
        c2 = Candy(name="Skittles", brand="Mars", price=3)
        c3 = Candy(name="Snickers", brand="Mars", price=3)

        db.session.add_all([c1, c2, c3])

        db.session.commit()
        #End of manual way

        #Loop way

        # for _ in range(1000):
        #     new_candy = Candy(name=faker.name(),brand = faker.address(), price = random.choice( range(1,7) ) )
        #     db.session.add( new_candy )
        # db.session.commit()

        for _ in range(500):
            new_country = Country(name=faker.country(), population = random.choice( range(10000,999999999)), area_code = random.choice( range(10,999)))
            db.session.add(new_country)
        db.session.commit()

        print("Candies are added the loop way")

        print("Seeding complete!")
