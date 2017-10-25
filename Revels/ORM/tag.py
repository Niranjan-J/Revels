from ORM.dbconnect import Connector

class Tag():
    def __init__(self):
        self.con=Connector()
    
    def createTable(self):
        self.con.create("""
            CREATE TABLE IF NOT EXISTS Tag( 
                text VARCHAR(200) NOT NULL
            );
        """)