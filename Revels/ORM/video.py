from ORM.dbconnect import Connector;


class Video():
    pass

class VideoManager():

    def __init__(self):

        #initiates the database Connector
        self.conn = Connector()

    def create_table(self):

        self.conn.query("""
            CREATE TABLE IF NOT EXISTS Video (
            video_id INTEGER AUTO_INCREMENT,
            title VARCHAR(200) NOT NULL ,
            descr TEXT(1000),
            url VARCHAR(200) NOT NULL ,
            img VARCHAR(200) NOT NULL ,
            user_id INT NOT NULL ,

            PRIMARY KEY (video_id),
            FOREIGN KEY (user_id) REFERENCES User(user_id)
            );""")
