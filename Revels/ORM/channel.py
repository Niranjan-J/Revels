from ORM.dbconnect import Connector

class Channel():
    def __init__(self):
        self.con=Connector()

    def createTable(self):
        self.con.query("""
            CREATE TABLE IF NOT EXISTS Channel( 
                channel_id INTEGER AUTO_INCREMENT,
                name VARCHAR(200) NOT NULL, 
                description VARCHAR(1000) NOT NULL, 
                PRIMARY KEY(channel_id), 
                user_id INT,
                FOREIGN KEY(user_id) REFERENCES User(user_id)
            );
        """)