from ORM.dbconnect import Connector

class Category():
    
    def __init__(self):
        self.con = Connector()

    def createTable(self):
        self.con.query("""
            CREATE TABLE IF NOT EXISTS Category(
                cat_id INTEGER AUTO_INCREMENT,
                text VARCHAR(200) NOT NULL,
                PRIMARY KEY(cat_id)
            );
        """)
