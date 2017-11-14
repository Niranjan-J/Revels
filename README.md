# Revels
DBMS minor project

Instructions on linux:
- Install LAMP server on the system.
- Create a database with utf8_unicode_ci character encoding.
- Create user with username django and password django. 
- If you want to configure the server and connection details open Revels/.env and edit the value for the variables.
-  Open the terminal, then navigate into Revels directory in the terminal now run the following command to create the databases : 
    python create.py
- Run the queries in triggers.sql to create the triggers.
- Run the queries in data.sql to create the sample database.
- Open the terminal, then navigate into Revels directory in the terminal now run the following command to install all dependencies : 
    sudo pip install -r req.txt
- In the terminal now run the following command to initiate the server :
    python manage.py runserver
- Open the browser and navigate to http://localhost:8000
