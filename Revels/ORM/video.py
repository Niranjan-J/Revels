from ORM.dbconnect import Connector

class Video():
    def __init__(self):
        #initiates the database Connector
        self.con = Connector()

    def createTable(self):
        self.con.create("""
            CREATE TABLE IF NOT EXISTS Video (
              video_id INTEGER AUTO_INCREMENT,
              title    VARCHAR(200) NOT NULL,
              descr    TEXT(1000),
              url      VARCHAR(200) NOT NULL,
              user_id  INT NOT NULL,

              PRIMARY KEY (video_id),
              UNIQUE (user_id, url, title),
              FOREIGN KEY (user_id) REFERENCES User (user_id)
            );
            """)

    def createTriggers(self):
      self.con.create(""" 
              Drop TRIGGER IF EXISTS videoDeleteTrigger;
              DELIMITER //
              CREATE TRIGGER videoDeleteTrigger
              BEFORE DELETE ON Video
                     FOR EACH ROW
                     BEGIN
                       DELETE FROM Tag WHERE OLD.video_id = video_id;
                       DELETE FROM Vid_Cat WHERE OLD.video_id = video_id;
                       DELETE FROM Pl_Vid WHERE OLD.video_id = video_id;
                       DELETE FROM Comment WHERE OLD.video_id = video_id;
                       DELETE FROM `Like` WHERE OLD.video_id = video_id;
                     END;//
            DELIMITER ;
        """)

    def insert(self,data):
        self.con.modify("""
            INSERT INTO Video(title, descr, url, user_id) VALUES (%s,%s,%s,%s)
            """ ,data['title'],data['descr'],data['url'],int(data['user_id']))

    def update(self,data):
        self.con.modify("""
            UPDATE Video SET title ="%s",descr ="%s",url ="%s",user_id ="%d"
            WHERE video_id = %d;
            """,data['video_id'],data['title'],data['descr'],data['url'],data['user_id'] )

    def remove(self,data):
        self.con.modify("""
            DELETE FROM Video WHERE video_id = %d
        """ , data['video_id'])

    def getallvideos(self):
        return self.con.query("SELECT * FROM Video;")

    def get_vid_id(self,data):
        return  self.con.query("SELECT video_id FROM Video WHERE url=%s",data['url'])

    def get_like(self,video_id,uid):
        res = self.con.query("SELECT * FROM `Like` WHERE video_id = %s AND user_id=%s",int(video_id),int(uid))
        if(len(res) > 0) :
            return True
        else :
            return False


