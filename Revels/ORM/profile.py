from ORM.dbconnect import Connector;


class Profile():
    pass

class ProfileManager():
    def __init__(self):

        #initiates the database Connector
        self.conn = Connector

    def create_table(self):
        self.conn.query("""
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
        res = self.conn.query("""
            SELECT * FROM Video WHERE user_id = %d;
        """, user_id)
        return res
