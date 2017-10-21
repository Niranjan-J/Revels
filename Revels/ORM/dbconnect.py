from django.db import connection

class Connector():
    def dictfetchall(self,cursor): 
        desc = cursor.description 
        return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
        ]

    def query(self, query, *args):
        #the *args here takes extra parameters with the query, and later the values are replaced in the query
        try:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(query,(args))
                    data=self.dictfetchall(cursor)
                    return data
                except Exception as e:
                    print(e)
                    return None
        except Exception as e:
                    print(e)
                    return None
        finally:
            pass
