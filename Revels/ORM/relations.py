from ORM.dbconnect import Connector

class Relationships():

    def __init__(self):
        #initiates the database Connector
        self.con = Connector()

    def create_UsersProfile(self) :
        self.con.create("""
            CREATE VIEW User_Profile AS
            SELECT * FROM User NATURAL JOIN Profile;
            """)

    def create_Vid_Cat(self):
        self.con.create("""
            CREATE TABLE IF NOT EXISTS Vid_Cat(
                video_id INT,
                cat_id INT,
                FOREIGN KEY(video_id) REFERENCES Video(video_id),
                FOREIGN KEY(cat_id) REFERENCES Category(cat_id)
            );
            """)

    def create_Subscription(self):
        self.con.create("""
            CREATE TABLE IF NOT EXISTS Subscription(
                user_id INT,
                channel_id INT,
                FOREIGN KEY(user_id) REFERENCES User(user_id),
                FOREIGN KEY(channel_id) REFERENCES Channel(channel_id)
            );
            """)

    def create_Like(self):
        self.con.create("""
            CREATE TABLE IF NOT EXISTS `Like`(
                video_id INT,
                user_id INT,
                FOREIGN KEY(video_id) REFERENCES Video(video_id),
                FOREIGN KEY(user_id) REFERENCES User(user_id)
            );
            """)

    def create_Pl_Vid(self):
        self.con.create("""
            CREATE TABLE IF NOT EXISTS Pl_Vid(
                video_id INT,
                playlist_id INT,
                UNIQUE(playlist_id,video_id),
                FOREIGN KEY(video_id) REFERENCES Video(video_id),
                FOREIGN KEY(playlist_id) REFERENCES Playlist(playlist_id)
            );
            """)
