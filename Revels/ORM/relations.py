from ORM.dbconnect import Connector

class Relationships():

    def __init__(self):
        #initiates the database Connector
        self.con = Connector()

        def create_UsersProfile(self) :
            self.con.query("""
                CREATE VIEW If NOT EXISTS User_Profile AS
                SELECT * FROM User NATURAL JOIN Profile;
                """)
