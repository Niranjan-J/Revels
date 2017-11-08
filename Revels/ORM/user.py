from ORM.dbconnect import Connector
from http.cookies import SimpleCookie
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

    def createTriggers(self):
        pass

    # returns user_id for a user data
    def getUserId(self,data):
        res = self.con.query("""
            SELECT * FROM `User` WHERE email = %s
            """,data['email']
            )
        return res[0]['user_id']

    #creates entry in USers and PRofile table
    def createUser(self,data):
        prf = Profile()
        #Creates Entry in users table
        res = self.insertUser(data)
        if res == None :
            # get's the user_id
            user_id = self.getUserId(data)
            #Creates Entry in profile table
            res1 = prf.createProfile(data,user_id)

            if res1 == None :
                return res1

            #returns None if the transaction completes without errors
            return None
        else :
            return res

    def signInUser(self,data):
        res = self.con.query("""
            SELECT * FROM `User` WHERE email = %s and password = %s
            """,data['email'],data['password']
            )
        if(len(res) == 1) :
            return True
        else :
            return False

    def insertUser(self,data):
        res = self.con.modify("""
            INSERT INTO User(email,username,password) VALUES (%s,%s,%s)
            """,data['email'],data['username'],data['password']
            )
        # returns None if there's no error
        if res == None :
            return None
        else :
            return res
