from ORM.dbconnect import Connector
from http.cookies import SimpleCookie
from ORM.user import User
from ORM.profile import Profile

class UserManager():

    def __init__(self):
        self.con = Connector()

    # This function performs validation checks on user data
    def validate(self,data):
        error = []
        if(data['email'] == None or data['email'] == '') :
            error.append("Please Enter an email address.")
        return error

    # returns user_id for a user data
    def getUserId(self,data):
        us = User()
        res = self.con.query("""
            SELECT * FROM `User` WHERE username = %s
            """,data['username']
            )
        return res[0][0];

    #creates entry in USers and PRofile table
    def createUser(self,data):

        #Creates Entry in users table
        usr = User()
        usr.createUser(data)

        # getes the user_id
        res = getUserId(data)

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
