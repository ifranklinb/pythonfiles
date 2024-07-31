# import pandas as pd
# import psycopg2
# from sqlalchemy import create_engine

# # Establish a connection to PostgreSQL
# conn = psycopg2.connect(
#     dbname="newdatabasedb",
#     user="postgres",
#     password="frank123",
#     host="localhost",
#     port="5432"
# )

# # Read the CSV file into a DataFrame
# csv_file_path = r'C:\Users\VC\Desktop\sql\datafiles\final_task\dev_wok_family_member_master.csv'
# df = pd.read_csv(csv_file_path)

# # Create a SQLAlchemy engine
# engine = create_engine('postgresql://postgres:frank123@localhost:5432/newdatabasedb')

# # Insert data into the existing table
# df.to_sql('dev_wok_family_member__master', engine, if_exists='append', index=False)

# # Commit changes and close connection
# conn.commit()
# conn.close()


import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Establish a connection to PostgreSQL
conn = psycopg2.connect(
    dbname="foode_local",
    user="postgres",
    password="frank123",
    host="localhost",
    port="5432"
)

# Read the CSV file into a DataFrame
csv_file_path = r'C:\Users\VC\Desktop\data-1721834518462_restaurants_master.csv'
df = pd.read_csv(csv_file_path)

# Create a SQLAlchemy engine
engine = create_engine('postgresql://postgres:frank123@localhost:5432/foode_local')

# Insert data into the existing table
df.to_sql('restaurants_master', engine, if_exists='append', index=False)

# df.to_sql('dev_wok_family_member_master', engine, if_exists='append', index=False)

# Commit changes and close connection
conn.commit()
conn.close()