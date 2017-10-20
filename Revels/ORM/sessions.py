from ORM.dbconnect import Connector;
import os
from Auth.user import UserManager;

class SessionsManager():

    def __init__(self):

        #initiates the database Connector
        self.conn = Connector()

    def createTable(self) :
        self.con.query("""
            CREATE TABLE Sessions (
                user_id INT,
                session_id VARCHAR(64),
                PRIMARY KEY (user_id),
                FOREIGN KEY (user_id) REFERENCES User(user_id)
            );
            """)

    def createSession(self,data) :
        s_id = str(os.urandom(16))
        userM = UserManager()
        user_id = userM.getUserId(data)
        self.conn.query("""
            INSERT INTO Sessions(user_id,session_id) values (%s,%s)
            """,int(user_id),s_id)
        return s_id;

    def checkSession(self,request) :
        s_id = request.COOKIES['session']
        res = self.conn.query("""
            SELECT * FROM Sessions WHERE session_id = %s
            """,s_id)
        if(len(res) == 1) :
            return True
        else :
            return False
