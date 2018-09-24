"""
Examples showing how to query database
Note that these tutorials are really just building on each other. Not very well
split out
"""

import Chapter2_Inserting_data as chp2Ins
from sqlalchemy.sql import select



if __name__ == '__main__':
    chp2Ins.start_engine()
    s = select([cookies])
    rp = connection.execute(s)
    results = rp.fetchall()

