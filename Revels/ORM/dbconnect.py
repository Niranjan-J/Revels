import MySQLdb
import gc


class Connector():

    def __init__(self):
        #connects to  the database server
        self.db = MySQLdb.connect(host="localhost", port=3306, user="django", passwd="django", db="django")
        #Initiates the cursor and defines it as a Dictionary cursor
        self.cursor = self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)

    def __del__(self):
        #destroys the object and closes the connection
        gc.collect()
        self.db.close()

    def query(self, query):
        try:
            try:

                no = self.cursor.execute(query)
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
