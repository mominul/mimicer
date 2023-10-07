# MIMICer
A frontend for viewing and manipulating MIMIC VI dataset
## Instructions
To run this project, these dependencies needs to be installed:

* Django
* mysql-connector-python
* mysqlclient
* numpy
* pandas

Afterwards create a database named `mimicer` in XAMPP's MySQL (through `myphpadmin`) and run following commands to start the project:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python db-upload.py csv_files_folder_path
python manage.py runserver
```
