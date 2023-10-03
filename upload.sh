#!/bin/bash

# MySQL configurations
USERNAME="root"
PASSWORD=""
DATABASE="mimicer2"
TABLE="app_admission"
XAMPP_PATH="/Applications/XAMPP/xamppfiles/bin"
CSV_PATH="/Users/mominul/Downloads/CSVs/admissions.csv"

# Check if CSV file exists
if [ ! -f "$CSV_PATH" ]; then
    echo "CSV file not found!"
    exit 1
fi

# Connect to MySQL and import CSV data
$XAMPP_PATH/mysql -u $USERNAME -p$PASSWORD $DATABASE -e "
LOAD DATA LOCAL INFILE '$CSV_PATH'
INTO TABLE $TABLE
FIELDS TERMINATED BY ','
ENCLOSED BY '\"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
" 2>&1

# Check if the command was successful
if [ $? -eq 0 ]; then
    echo "CSV imported successfully into $TABLE."
else
    echo "There was an error importing the CSV."
    exit 1
fi
