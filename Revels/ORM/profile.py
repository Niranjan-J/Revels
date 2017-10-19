from ORM.dbconnect import Connector

class Profile():
    def __init__(self):
        self.con = Connector()

    def createTable(self):
        self.con.query("""
            CREATE TABLE IF NOT EXISTS User (
            user_id INTEGER AUTO_INCREMENT,
            firstname VARCHAR(50) NOT NULL ,
            lastname VARCHAR(50) ,
            avatar VARCHAR(200) NOT NULL ,

            PRIMARY KEY (user_id),
            UNIQUE (firstname, lastname, avatar),
            FOREIGN KEY (user_id) REFERENCES User (user_id)
            );
            """)

    def getAllVideosOfUser(self, user_id) :
        return  self.con.query("""
            SELECT * FROM Video WHERE user_id = %d;
            """, user_id)
