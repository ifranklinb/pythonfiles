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
# csv_file_path = r'C:\Users\VC\Desktop\sql\datafiles\final_task\dev_wok_family_master.csv'
# # Create a cursor object
# cur = conn.cursor()

# # Create a SQLAlchemy engine
# engine = create_engine('postgresql://postgres:frank123@localhost:5432/newdatabasedb')

# # Replace 'table_name' with the name you want to give to your table in the PostgreSQL database
# df.to_sql('dev_wok_family_master', engine, if_exists='replace', index=False)

# # Commit changes and close connection
# conn.commit()
# conn.close()



import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Establish a connection to PostgreSQL
conn = psycopg2.connect(
    dbname="newdatabasedb",
    user="postgres",
    password="frank123",
    host="localhost",
    port="5432"
)

# Read the CSV file into a DataFrame
csv_file_path = r'C:\Users\VC\Desktop\sql\datafiles\final_task\prod_family_member_master.csv'
df = pd.read_csv(csv_file_path)

# Create a SQLAlchemy engine
engine = create_engine('postgresql://postgres:frank123@localhost:5432/newdatabasedb')

# Replace 'table_name' with the name you want to give to your table in the PostgreSQL database
df.to_sql('prod_wok_family_member_master', engine, if_exists='replace', index=False)

# Commit changes and close connection
conn.commit()
conn.close()
