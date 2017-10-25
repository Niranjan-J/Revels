from ORM.dbconnect import Connector
from Auth.user import UserManager
import os

class SessionsManager():

    def __init__(self):
        #initiates the database Connector
        self.conn = Connector()

    def createTable(self) :
        self.conn.create("""
            CREATE TABLE If NOT EXISTS Sessions (
                user_id INT,
                session_id VARCHAR(64),
                PRIMARY KEY (user_id),
                FOREIGN KEY (user_id) REFERENCES User(user_id)
            );
            """)

    # Inserts Session data into the sessions table and returns an unique session id
    def insertSession(self,data,userM):
        s_id = str(os.urandom(16))
        user_id = userM.getUserId(data)
        self.conn.modify("""
            INSERT INTO Sessions(user_id,session_id) values (%s,%s)
            """,int(user_id),s_id)
        return s_id

    # Creates a session and creates the sessions cookies
    def createSession(self,data,response) :

        userM = UserManager()
        if(userM.signInUser(data)) :
            s_id = self.insertSession(data,userM)
            response.set_cookie('session', s_id)
            return True
        else :
            return False


    # checks the request for the sessions cookies and matches it with the sessions table
    def checkSession(self,request) :
        s_id = request.COOKIES['session']
        res = self.conn.query("""
            SELECT User_Profile.* FROM
            Sessions NATURAL JOIN User_Profile
            WHERE session_id = %s
            """,s_id)
        if(len(res) == 1) :
            return res
        else :
            return None
