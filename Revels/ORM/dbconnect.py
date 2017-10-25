from django.db import connection, transaction

class Connector():
    
    def dictfetchall(self,cursor):
        # Return all rows from a cursor as a dict
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    def checkdict(self,data):
        #check whether dictionary or not 
        if type(data) is dict:
            return True
        else:
            return False
    
    def create(self,sqlquery):
        try:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(sqlquery)
                except Exception as e:
                    print(e)
        finally:
            pass

    def modify(self,sqlquery,*args):
        try:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(sqlquery,args)
                    print("Sucessfully Modified.")
                except Exception as e:
                    return e
        finally:
            pass

    def query(self,sqlquery,*args):
        try:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(sqlquery,args)
                    data=self.dictfetchall(cursor)
                    print("Query Sucessfully Executed.")
                    return data
                except Exception as e:
                    return e
        finally:
            pass