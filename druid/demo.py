# pip install pydruid
# # or, if you intend to use asynchronous client
# pip install pydruid[async]
# # or, if you intend to export query results into pandas
# pip install pydruid[pandas]
# # or, if you intend to do both
# pip install pydruid[async, pandas]
# # or, if you want to use the SQLAlchemy engine
# pip install pydruid[sqlalchemy]
# # or, if you want to use the CLI
# pip install pydruid[cli]

from pydruid.client import *
from pylab import plt
from pydruid.db import connect

conn = connect(host='192.168.11.127', port=32666, path='/druid/v2/sql/', scheme='http')
curs = conn.cursor()
curs.execute("""
    SELECT place,
           CAST(REGEXP_EXTRACT(place, '(.*),', 1) AS FLOAT) AS lat,
           CAST(REGEXP_EXTRACT(place, ',(.*)', 1) AS FLOAT) AS lon
      FROM places
     LIMIT 10
""")

for row in curs:
    print(row)