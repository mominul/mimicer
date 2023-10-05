import pandas as pd
import numpy as np
import mysql.connector
import sys

# python db-upload.py table_name csv_file_path

# MySQL database connection parameters
db_config = {
    'host': 'localhost',      # Your MySQL server host (usually 'localhost')
    'user': 'root',           # MySQL username
    'password': '',           # MySQL password (if any)
    'database': 'mimicer2',    # Your target database
}

# CSV file path
csv_file = sys.argv[2]
table_name = sys.argv[1]

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(csv_file)

# Replace NaN values with None (NULL) in the DataFrame
#df = df.where(pd.notna(df), None)
df = df.replace({np.nan: None})

# Establish a connection to the MySQL database
try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Get the list of table columns from the MySQL database
    cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}' AND COLUMN_NAME != 'id'")
    columns = [row[0] for row in cursor.fetchall()]
    # Remove Duplicates
    columns = list(dict.fromkeys(columns))
    # Rearrange the DataFrame columns to match the MySQL table's column order
    df = df[columns]

    # Insert the data into the MySQL table
    for index, row in df.iterrows():
        values = tuple(row)
        placeholders = ', '.join(['%s'] * len(values))
        insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
        cursor.execute(insert_query, values)

    # Commit the changes and close the database connection
    connection.commit()
    print("Data import successful!")

except mysql.connector.Error as error:
    print(f"Error: {error}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
