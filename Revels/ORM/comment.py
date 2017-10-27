from ORM.dbconnect import Connector

class Comment():
    def __init__(self):
        self.con=Connector()

    def createTable(self):
        self.con.query("""
            CREATE TABLE IF NOT EXISTS Comment(
                comment_id INTEGER NOT NULL AUTO_INCREMENT KEY ,
                text VARCHAR(2000),
                timestamp TIMESTAMP NOT NULL,
                video_id INT,
                user_id INT,
                FOREIGN KEY(video_id) REFERENCES Video(video_id),
                FOREIGN KEY(user_id) REFERENCES User(user_id)
            );
        """)
