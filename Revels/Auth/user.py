from ORM.dbconnect import Connector

class UserManager():

    def __init__(self):
        self.con = Connector()

    def checkUserData(self,data):
        error = []
        if(data['email'] == None or data['email'] == '') :
            error.append("Please Enter an email address.")
        return error

    def createUser(self,data):
        self.con.query("""
            INSERT INTO User(email,username,password) VALUES (%s,%s,%s)
            """,data['email'],data['username'],data['password']
            )
        res = self.con.query("""
            SELECT * FROM `User` WHERE username = %s
            """,data['username']
            )
        print(res)
        self.con.query("""
            INSERT INTO Profile(user_id,firstname,lastname,gender,avatar) VALUES (%s,%s,%s,%s,%s)
            """,res[0][0],data['firstname'],data['lastname'],data['gender'],"Please change it"
            )

    def signInUser(self,data):
        pass
