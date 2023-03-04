import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, String

engine = create_engine('sqlite:///bazatest.db')

meta = MetaData()

# Define the stations table
stations = Table('stations', meta,
    Column('id', String, primary_key=True),
    Column('name', String),
    Column('latitude', String),
    Column('longitude', String),
    Column('elevation', String),
    Column('state', String),
    Column('country', String)
)

# Load data from the CSV file into the stations table
df = pd.read_csv('clean_stations.csv', dtype={
    'id': str,
    'name': str,
    'latitude': str,
    'longitude': str,
    'elevation': str,
    'state': str,
    'country': str
})

with engine.connect() as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS stations (id TEXT PRIMARY KEY, name TEXT, latitude TEXT, longitude TEXT, elevation TEXT, state TEXT, country TEXT)")

    conn.execute(stations.insert(), df.to_dict(orient='records'))

# Select and fetch the first 5 rows from the stations table
with engine.connect() as conn:
    result = conn.execute("SELECT * FROM stations ORDER BY id LIMIT 5").fetchall()
    print(result)



