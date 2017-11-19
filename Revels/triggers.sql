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

            DROP TRIGGER IF EXISTS checkUserInsert;
                        DELIMITER //
                        CREATE TRIGGER checkUserInsert
                        BEFORE INSERT ON User
                        FOR EACH ROW
                        BEGIN
                          DECLARE msg VARCHAR(100);
                          IF UPPER(NEW.email) NOT LIKE '%_@_%._%' THEN
                            set msg = "Please enter a valid email address";
                            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
                          END IF ;
                            IF UPPER(NEW.username) = '' OR UPPER(NEW.username) = NULL THEN
                set msg = "Please enter an Username";
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
              END IF ;
                        END//
                          DELIMITER ;



            DROP TRIGGER IF EXISTS checkProfileInsert;
            DELIMITER //
            CREATE TRIGGER checkProfileInsert
            BEFORE INSERT ON Profile
            FOR EACH ROW
            BEGIN
              DECLARE msg VARCHAR(100);
              IF UPPER(NEW.firstname) = '' OR UPPER(NEW.firstname) = NULL THEN
                DELETE FROM User WHERE User.user_id = NEW.user_id;
                set msg = "Please enter a Firstname";
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
              END IF ;
               IF UPPER(NEW.lastname) = '' OR UPPER(NEW.lastname) = NULL THEN
                DELETE FROM User WHERE User.user_id = NEW.user_id;
                set msg = "Please enter a Lastname";
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
              END IF ;

            END//
