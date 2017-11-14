     Drop TRIGGER IF EXISTS channelDeleteTrigger;

                DELIMITER //
                CREATE TRIGGER channelDeleteTrigger
                BEFORE DELETE ON Channel
                       FOR EACH ROW

                       BEGIN
                         DELETE FROM Playlist WHERE OLD.channel_id = channel_id;
                         DELETE FROM Subscription WHERE OLD.channel_id = channel_id;
                       END//
                DELIMITER ;

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

Drop TRIGGER IF EXISTS playlistDeleteTrigger;
            DELIMITER //
            CREATE TRIGGER playlistDeleteTrigger
            BEFORE DELETE ON Playlist
            FOR EACH ROW
            BEGIN
            DELETE FROM Pl_Vid WHERE OLD.playlist_id = playlist_id;
            END;//
            DELIMITER ;