from ORM.dbconnect import Connector

class Playlist():
    def __init__(self):
        self.con = Connector()

    def createTable(self):
        self.con.query("""
            CREATE TABLE IF NOT EXISTS Playlist( 
                playlist_id INTEGER NOT NULL,
                name VARCHAR(200) NOT NULL,
                channel_id INT,
                FOREIGN KEY (channel_id) REFERENCES Channel (channel_id)
            );
        """)