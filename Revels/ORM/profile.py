from ORM.dbconnect import Connector

class Profile():
    def __init__(self):
        self.con = Connector()

    def createTable(self):
        self.con.query("""
            CREATE TABLE IF NOT EXISTS Profile(
            user_id INT,
            firstname VARCHAR(50) NOT NULL ,
            lastname VARCHAR(50) ,
            gender VARCHAR(1) ,
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

    def createProfile(self,data):
        self.con.query("""
            INSERT INTO Profile(user_id,firstname,lastname,gender,avatar) VALUES (%s,%s,%s,%s,%s)
            """,res,data['firstname'],data['lastname'],data['gender'],"Please change it"
            )
