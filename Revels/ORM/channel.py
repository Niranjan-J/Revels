from ORM.dbconnect import Connector

class Channel():
    def __init__(self):
        self.con=Connector()

    def createTriggers(self):
        self.con.create(""" 

                Drop TRIGGER IF EXISTS channelDeleteTrigger;

                DELIMITER //
                CREATE TRIGGER channelDeleteTrigger
                BEFORE DELETE ON Channel
                       FOR EACH ROW

                       BEGIN
                         DELETE FROM Playlist WHERE OLD.channel_id = channel_id;
                         DELETE FROM Subscription WHERE OLD.channel_id = channel_id;
                       END//

            """)

    def createTable(self):
        self.con.create("""
            CREATE TABLE IF NOT EXISTS Channel( 
                channel_id INTEGER AUTO_INCREMENT,
                name VARCHAR(200) NOT NULL, 
                description VARCHAR(1000) NOT NULL, 
                PRIMARY KEY(channel_id), 
                user_id INT,
                FOREIGN KEY(user_id) REFERENCES User(user_id)
            );
        """)
