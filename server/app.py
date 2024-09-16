#!/usr/bin/env python3

from flask import request
from config import app, db
from models import Candy, Country
# from models import MODELS GO HERE


# ROUTES

@app.get('/')
def index():
    return { "response": "hello world" }, 200

# CREATE

#Candy
@app.post('/candies')
def add_candy():
    data = request.json ## Need
    try:
        # Make instance
        # new_candy = Candy(name=data["name"], brand=data["brand"], price = data["price"])
        new_candy = Candy(**data) #short hand, key value pairs need to be identical
        
        # add/commit the instance
        db.session.add(new_candy)
        db.session.commit()

        #return the candy
        return new_candy.to_dict(), 201
    except Exception as e:
        return {"error": str(e)}, 404

#Country
@app.post('/countries')
def add_country():
    data = request.json
    try:
        new_country = Country(**data)
        db.session.add(new_country)
        db.session.commit()
        return new_country.to_dict(), 201
    except Exception as e:
        return {"error": "invalid data"}, 404

# READ ALL

#Candy
@app.get('/candies')
def all_candies():
    all_the_candies = Candy.query.all()

    # candy_dictionaries = []

    # for candy in all_the_candies:
    #     candy_dict = candy.to_dict()
    #     candy_dictionaries.append( candy_dict )
    # return candy_dictionaries, 200

    #list comprehension
    return [ candy.to_dict() for candy in all_the_candies ]

#Country
@app.get('/countries')
def all_countries():
    all_the_countries = Country.query.all()
    return [country.to_dict() for country in all_the_countries]

# READ BY ID

@app.get('/candies/<int:id>')
def candy_by_id(id):
    found_candy = Candy.query.where(Candy.id == id).first()

    if found_candy:
        return found_candy.to_dict(), 200
    else:
        return {'error':"candy not found"}, 404
    
#Country

@app.get('/countries/<int:id>')
def country_by_id(id):
    found_country = Country.query.where(Country.id == id).first()

    try:
        return found_country.to_dict(), 200
    except TypeError:
        return {"error":"can't find country"}, 404



# UPDATE

@app.patch('/candies/<int:id>')
def update_candy(id):
    candy_to_update = Candy.query.where(Candy.id == id).first()

    if candy_to_update:
        
        try:

            data = request.json ## Need

            #below allows to account for any number of key value item pairs
            for key in data:
                setattr(candy_to_update, key, data[key])
                #setattr(candy_to_update, "name", "reeses")
            
            db.session.add(candy_to_update)
            db.session.commit()

            return candy_to_update.to_dict(), 202
        
        except Exception as e:
            return {"error":str(e)}, 400


    else:
        return {"error":"does not exist"}, 404




# DESTROY
#Candy
@app.delete('/candies/<int:id>')
def delete_candy(id):
    candy_to_delete = Candy.query.where(Candy.id == id).first()
    try:
        db.session.delete( candy_to_delete )
        db.session.commit()

        return {}, 204
    
    except:
        return {'error':'Not Found'}, 404

#Country
@app.delete('/countries/<int:id>')
def delete_country(id):
    country_to_delete = Country.query.where(Country.id == id).first()
    try:
        db.session.delete( country_to_delete )
        db.session.commit()
        return {}, 204
    
    except:
        return {'error':'Not Found'}, 404





# APP RUN

if __name__ == '__main__':
    app.run(port=5555, debug=True)