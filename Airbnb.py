CREATE TABLE host (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    money_received INT NOT NULL
);

INSERT INTO host VALUES (1, 'Jenny', 2500), (2, 'Vlad', 395), (3, 'Inna', 100);

CREATE TABLE room (
    id INT NOT NULL PRIMARY KEY,
    host_id INT NOT NULL,
    residents INT NOT NULL,
    price_per_night INT NOT NULL,
    room_square INT NOT NULL,
    A/C BOOLEAN NOT NULL,
    free_wi_fi BOOLEAN NOT NULL,
    room_service BOOLEAN NOT NULL,
    indoor_service BOOLEAN NOT NULL,
    indoor_kitchen BOOLEAN NOT NULL,
    is_available BOOLEAN NOT NULL,

    FOREIGN KEY (host_id)
        REFERENCES host (id) 
);

INSERT INTO room (id, host_id, residents, price_per_night, room_square, A_C, free_wi_fi, room_service, indoor_service, indoor_kitchen, is_available) VALUES (1, 2, 150, 64, TRUE, TRUE, TRUE, FALSE, TRUE, TRUE), (2, 1, 35, 18, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE), (3, 4, 25, 32, FALSE, FALSE, FALSE, TRUE, TRUE, TRUE);

CREATE TABLE guest (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    payment_balance INT NOT NULL,
    rooms_reserved INT NOT NULL
);

INSERT INTO guest VALUES ("Mike", 550, 1), ("Sontsedar", 1000, 2), ("Scrouge", 50, 1)

CREATE TABLE host_review (
    id INT NOT NULL PRIMARY KEY,
    guest_id INT NOT NULL,
    host_id INT NOT NULL,
    host_rating INT NOT NULL,

    FOREIGN KEY (host_id)
        REFERENCES host (id)
    FOREIGN KEY (guest_id)
        REFERENCES guest (id)
);

INSERT INTO host_review VALUES (2, 3, 7), (2, 1, 10), (1, 2, 8)

CREATE TABLE room_reservation (
    id INT NOT NULL PRIMARY KEY,
    guest_id INT NOT NULL,
    room_id INT NOT NULL,
    room_reserved BOOLEAN NOT NULL,
    room_paid BOOLEAN NOT NULL,

    FOREIGN KEY (guest_id)
        REFERENCES guest (id)
    FOREIGN KEY (room_id)
        REFERENCES room (id)
);

INSERT INTO room_reservation VALUES (2, 3, TRUE, TRUE), (2, 1, TRUE, TRUE), (1, 2, TRUE, TRUE)

# Task_1

SELECT name, id, rooms_reserved FROM guest ORDER BY rooms_reserved desc LIMIT 1

# Task_2

SELECT name, id FROM host ORDER BY money_received

# Task_3

SELECT host_id FROM host_review WHERE MAX(host_rating)

