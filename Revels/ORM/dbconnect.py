import MySQLdb
import gc
import environ

# Enviroinment Variables
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')

class Connector():

    def __init__(self):
        #connects to  the database server
        self.db = MySQLdb.connect(host=env.str('DATABASE_HOST'), port=env.int('DATABASE_PORT'), user=env.str('DATABASE_USER'), passwd=env.str('DATABASE_PASSWORD'), db=env.str('DATABASE_NAME'))
        #Initiates the cursor and defines it as a Dictionary cursor
        self.cursor = self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)

    def __del__(self):
        #destroys the object and closes the connection
        gc.collect()
        self.db.close()

    def commit(self):
        #commits must be done to store the changes, eg:  insert operations wont be noticed in the table otherwise
        self.db.commit()

    def query(self, query, *args):
        #the *args here takes extra parameters with the query, and later the values are replaced in the query 
        try:
            try:
                no = self.cursor.execute(query,(args))
                data = self.cursor.fetchall()

                if no == None or no == 0 :
                    return None
                else :
                    return data

            except (MySQLdb.Error, MySQLdb.Warning) as e:
                print(e)
                return None

        finally:
            pass
