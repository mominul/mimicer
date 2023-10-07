import pandas as pd
import numpy as np
import mysql.connector
import sys

# python db-upload.py csv_files_folder_path

# MySQL database connection parameters
db_config = {
    'host': 'localhost',      # Your MySQL server host (usually 'localhost')
    'user': 'root',           # MySQL username
    'password': '',           # MySQL password (if any)
    'database': 'mimicer',    # Your target database
}

def export_to_database(csv_file, table_name, mapping):
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file)

    # Replace NaN values with None (NULL) in the DataFrame
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
        # Rename the columns using the dictionary
        if mapping:
            df.rename(columns=mapping, inplace=True)
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
        print(f"Data import for {table_name} is successful!")

    except mysql.connector.Error as error:
        print(f"Error for {table_name}: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

export_to_database(f'{sys.argv[1]}/patients.csv', 'app_patient', {})
export_to_database(f'{sys.argv[1]}/admissions.csv', 'app_admission', { 'subject_id': 'subject_id_id' })
export_to_database(f'{sys.argv[1]}/edstays.csv', 'app_edstay', { 'subject_id': 'subject_id_id', 'hadm_id': 'hadm_id_id' })
export_to_database(f'{sys.argv[1]}/diagnosis.csv', 'app_diagnosis', { 'subject_id': 'subject_id_id', 'stay_id': 'stay_id_id' })
export_to_database(f'{sys.argv[1]}/pyxis.csv', 'app_pyxis', { 'subject_id': 'subject_id_id', 'stay_id': 'stay_id_id' })
export_to_database(f'{sys.argv[1]}/triage.csv', 'app_triage', { 'subject_id': 'subject_id_id', 'stay_id': 'stay_id_id' })