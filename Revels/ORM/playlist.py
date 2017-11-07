from ORM.dbconnect import Connector

class Playlist():
    def __init__(self):
        self.con = Connector()

    def createTriggers(self):
        self.con.create("""
        Drop TRIGGER IF EXISTS playlistDeleteTrigger;

              DELIMITER //
              CREATE TRIGGER playlistDeleteTrigger
              BEFORE DELETE ON Playlist
                     FOR EACH ROW

                     BEGIN
                       DELETE FROM Pl_Vid WHERE OLD.playlist_id = playlist_id;
                     END//
        """)

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
