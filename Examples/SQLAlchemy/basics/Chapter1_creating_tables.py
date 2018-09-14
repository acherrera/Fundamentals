
from datetime import datetime
from sqlalchemy import (DateTime, Table, Column, Integer, Numeric, String,
                        ForeignKey, MetaData, create_engine, Boolean)

# Start the metdata handler
metadata=MetaData()

# Basic Table for cookie 
cookees = Table('cookies', metadata,
        Column('cookie_id', Integer(), primary_key=True),
        Column('cookie_name', String(50), index=True),
        Column('cookie_receipe_url', String(255)),
        Column('cookie_sku', String(55)),
        Column('quantity', Integer()),
        Column('unit_cost', Numeric(12,2))
)
        # Number: Takes maximum and decimal places. Ex: $XX.XX


# More advanced table for users
users = Table('users', metadata,
    Column('user_id', Integer(), primary_key=True),
    Column('customer_number', Integer(), autoincrement=True),
    Column('username', String(15), nullable=False, unique=True),
    Column('email_address', String(255), nullable=False),
    Column('phone', String(20), nullable=False),
    Column('password', String(25), nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now,
        onupdate=datetime.now)
)

# Now Get into the relational part!
orders = Table('orders', metadata,
    Column('order_id', Integer(), primary_key=True),
    Column('user_id', ForeignKey('users.user_id')),
    Column('shipped', Boolean(), default=False)
)

line_items = Table('line_items', metadata,
    Column('line_items_id', Integer(), primary_key=True),
    Column('order_id', ForeignKey('orders.order_id')),
    Column('cookie_id', ForeignKey('cookies.cookie_id')),
    Column('quantity', Integer()),
    Column('extended_cost', Numeric(12,2))
)


if __name__ == '__main__':
    # Not create the schema
    engine = create_engine('sqlite://')
    metadata.create_all(engine)
