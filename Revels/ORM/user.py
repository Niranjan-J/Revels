from ORM.dbconnect import Connector
from http.cookies import SimpleCookie
from ORM.user import User
from ORM.profile import Profile


class User():

    def __init__(self):
        self.con = Connector()

    def createTable(self):
        self.con.create("""
            CREATE TABLE IF NOT EXISTS User (
            user_id INTEGER AUTO_INCREMENT ,
            username VARCHAR(50) NOT NULL UNIQUE ,
            email VARCHAR(50) NOT NULL UNIQUE ,
            password VARCHAR(200) NOT NULL ,

            PRIMARY KEY (user_id),
            UNIQUE (username, email, password)
            );
            """)

    # returns user_id for a user data
    def getUserId(self,data):
        us = User()
        res = self.con.query("""
            SELECT * FROM `User` WHERE username = %s
            """,data['username']
            )
        return res[0]['user_id']

    #creates entry in USers and PRofile table
    def createUser(self,data):

        #Creates Entry in users table
        self.insertUser(data)

        # get's the user_id
        res = self.getUserId(data)

        #Creates Entry in profile table
        prf = Profile()
        prf.createProfile(data)

    def signInUser(self,data):
        res = self.con.query("""
            SELECT * FROM `User` WHERE username = %s and password = %s
            """,data['username'],data['password']
            )
        if(len(res) == 1) :
            return True
        else :
            return False

    def insertUser(self,data):
        self.con.query("""
            INSERT INTO User(email,username,password) VALUES (%s,%s,%s)
            """,data['email'],data['username'],data['password']
            )
