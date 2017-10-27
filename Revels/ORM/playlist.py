from ORM.dbconnect import Connector

class Playlist():
    def __init__(self):
        self.con = Connector()

    def createTable(self):
        self.con.create("""
            CREATE TABLE IF NOT EXISTS Playlist( 
                playlist_id INT AUTO_INCREMENT,
                name VARCHAR(200) NOT NULL,
                channel_id INT,
                PRIMARY KEY(playlist_id),
                FOREIGN KEY(channel_id) REFERENCES Channel (channel_id)
            );
        """)