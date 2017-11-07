from ORM.dbconnect import Connector
from ORM.user import User
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

    def createTriggers(self):
        pass

    # Inserts Session data into the sessions table and returns an unique session id
    def insertSession(self,data,user):
        s_id = str(os.urandom(16))
        user_id = user.getUserId(data)

        #Deletes previous sessions of the user
        self.conn.modify("""
            DELETE FROM Sessions WHERE user_id = %s
        """, int(user_id))

        # inserts the session data
        res = self.conn.modify("""
            INSERT INTO Sessions(user_id,session_id) values (%s,%s)
            """, int(user_id), s_id)

        if res == None :
            return s_id
        else :
            return None

    # Creates a session and creates the sessions cookies
    def createSession(self,data,response) :

        user = User()
        if(user.signInUser(data)) :
            s_id = self.insertSession(data,user)
            response.set_cookie('session', s_id)
            return response
        else :
            return None


    # checks the request for the sessions cookies and matches it with the sessions table
    def checkSession(self,request) :
        try :
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
        except :
            return None
