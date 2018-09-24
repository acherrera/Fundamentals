"""
Following along with book on inserting data
"""

from Chapter1_creating_tables import *
from sqlalchemy import insert
from pprint import pprint
from sqlalchemy.sql import select

# Example insert method
ins = cookies.insert().values(
        cookie_name="chocolate_chip",
        cookie_receipe_url="http://some.awso.me/cookie/receipe.html",
        cookie_sku="CC01",
        quantity="12",
        unit_cost="0.50"
)


# print(str(ins)) #Show command being issued
# pprint(ins.compile().params) #Pretty show
# result = connection.execute(ins) # Add to DB

# ins = cookies.insert()
# 
# result = connection.execute(
#        ins,
#        cookie_name="dark chocolate_chip",
#        cookie_receipe_url="http://some.awso.me/cookie/receipe_dark.html",
#        cookie_sku="CC02",
#        quantity="1",
#        unit_cost="0.75"
#)

# result.inserted_primary_key # This will get result


# Insert all the data
inventory_list = [
        {
            'cookie_name':"dark chocolate_chip",
            'cookie_receipe_url':"http://some.awso.me/cookie/receipe_dark.html",
            'cookie_sku':"CC02",
            'quantity':"1",
            'unit_cost':"0.75"
        },
        {
            'cookie_name':"dark chocolate_chip",
            'cookie_receipe_url':"http://some.awso.me/cookie/receipe_dark.html",
            'cookie_sku':"CC02",
            'quantity':"1",
            'unit_cost':"0.75"
        }
]


def start_engine(location='sqlite://'):
    # Where to insert and what to insert - keys must be exactly the same
    engine = create_engine('sqlite://')
    # Create the schema as defined previously
    # Metadata part was created before and imported
    metadata.create_all(engine)
    connection = engine.connect()


if __name__ == '__main__':

    # Where to insert and what to insert - keys must be exactly the same
    engine = create_engine('sqlite://')
    # Create the schema as defined previously
    # Metadata part was created before and imported
    metadata.create_all(engine)
    connection = engine.connect()
    result = connection.execute(ins, inventory_list)

    s = select([cookies])
    rp = connection.execute(s)
    results = rp.fetchall()

    pprint(results)


