from ORM.dbconnect import Connector;


class User():
    pass

class UserManager():

    def __init__(self):

        #initiates the database Connector
        self.conn = Connector

    def create_table(self):
        self.conn.query("""
            CREATE TABLE IF NOT EXISTS User (
            user_id INTEGER AUTO_INCREMENT,
            username VARCHAR(50) NOT NULL ,
            email VARCHAR(50) NOT NULL ,
            password VARCHAR(200) NOT NULL ,

            PRIMARY KEY (user_id)
            );
            """)
