from ORM.dbconnect import Connector

class Tag():
    def __init__(self):
        self.con=Connector()

    def createTable(self):
        self.con.create("""
            CREATE TABLE IF NOT EXISTS Tag(
                video_id INT,
                tag VARCHAR(200) NOT NULL UNIQUE,
                PRIMARY KEY (video_id,tag),
                FOREIGN KEY (video_id) REFERENCES Video(video_id)
            );
        """)

    def createTriggers(self):
        pass

    def create_Procs(self):
        self.con.create("""
            CREATE PROCEDURE insertTag( IN tag VARCHAR(100), IN video_id INT )
              BEGIN
                INSERT INTO Tag(video_id, tag) VALUES(video_id, tag) ;
              END
        """)

    def insertTags(self,tags,video_id):
        tags = tags.split(',')
        for tag in tags:
            self.con.callProc('insertTag',tag,video_id)
