from django.db import connection

class Connector():
    def query(self, query, *args):
        #the *args here takes extra parameters with the query, and later the values are replaced in the query
        try:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(query,(args))
                    data=cursor.fetchall()
                    return data
                except Exception as e:
                    print(e)
                    return None
        except Exception as e:
                    print(e)
                    return None
        finally:
            pass
