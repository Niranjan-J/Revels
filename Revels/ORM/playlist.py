from ORM.dbconnect import Connector

class Playlist():
    def __init__(self):
        self.con = Connector()

    def createTable(self):
        self.con.query("""
            CREATE TABLE IF NOT EXISTS Playlist( 
                playlist_id INTEGER AUTO_INCREMENT NOT NULL,
                name VARCHAR(200) NOT NULL,
                FOREIGN KEY (channel_id) REFERENCES Channel (channel_id)
            );
        """)