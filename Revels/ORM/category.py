from ORM.dbconnect import Connector

class Category():

    def __init__(self):
        self.con = Connector()

    def createTable(self):
        self.con.create("""
            CREATE TABLE IF NOT EXISTS Category(
                cat_id INTEGER AUTO_INCREMENT,
                text VARCHAR(200) NOT NULL,
                PRIMARY KEY(cat_id)
            );
        """)

    def createTriggers(self):
        pass

    def insert(self, data):
        self.con.modify("""
            INSERT INTO Category(text)
            VALUES(%s);
        """,data["text"])

    def getall(self):
        return self.con.query("SELECT * FROM Category;")

    def get_CatVideos(self,catname):
        res = self.con.query("""
            SELECT Video.*,Category.text FROM Video,Category,Vid_Cat
            WHERE Video.video_id=Vid_Cat.Video_id
            AND Vid_Cat. cat_id=Category.cat_id AND Category.text=%s
            ;""",catname)
        return res
