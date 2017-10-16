from ORM.dbconnect import Connector;

class VideoManager():

    def __init__(self):

        #initiates the database Connector
        self.conn = Connector()

    def createTable(self):

        self.conn.query("""
            CREATE TABLE IF NOT EXISTS Video (
              video_id INTEGER AUTO_INCREMENT,
              title    VARCHAR(200) NOT NULL,
              descr    TEXT(1000),
              url      VARCHAR(200) NOT NULL,
              img      VARCHAR(200) NOT NULL,
              user_id  INT          NOT NULL,

              PRIMARY KEY (video_id),
              UNIQUE (user_id, url, title, img),
              FOREIGN KEY (user_id) REFERENCES User (user_id)
            );
            """)

    def getAllVideosOfUser(self, user_id) :
        res = self.conn.query("""
            SELECT * FROM Video WHERE user_id = %d;
        """, user_id)
        videoLi = []
        #creates video list
        for row in res :
            videoLi.append(Video(row))
        return videoLi


    def insert(self,data):
        self.conn.query("""
            INSERT INTO Video(title, descr, url, img, user_id) VALUES (%s,%s,%s,%s,%s)
            """ ,self.data['title'],self.data['descr'],self.data['url'],self.data['img'],int(self.data['user_id']))
        self.conn.commit()

    def update(self,data):
        self.conn.query("""
            UPDATE Video SET title ="%s",descr ="%s",url ="%s",img ="%s",user_id ="%d"
            WHERE video_id = %d;
            """,self.data['video_id'],self.data['title'],self.data['descr'],self.data['url'],self.data['img'],self.data['user_id'] )
        self.conn.commit()

    def remove(self,data):
        self.conn.query("""
            DELETE FROM Video WHERE video_id = %d
        """ , self.data['video_id'])
        self.__del__()
