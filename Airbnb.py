CREATE TABLE host (
    id serial PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    money_received INT NOT NULL
);

INSERT INTO host VALUES ("Jenny", 2500), ("Vlad", 395), ("Inna", 100);

CREATE TABLE room (
    id serial PRIMARY KEY,
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

INSERT INTO room VALUES (1, 2, 150, 64, TRUE, TRUE, TRUE, FALSE, TRUE, TRUE), (2, 1, 35, 18, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE), (3, 4, 25, 32, FALSE, FALSE, FALSE, TRUE, TRUE, TRUE);

CREATE TABLE guest (
    id serial PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    payment_balance INT NOT NULL,
    rooms_reserved INT NOT NULL
);

INSERT INTO guest VALUES ("Mike", 550, 1), ("Sontsedar", 1000, 2), ("Scrouge", 50, 1)

CREATE TABLE host_review (
    id serial PRIMARY KEY,
    guest_id INT NOT NULL,
    host_id INT NOT NULL,
    host_rating INT NOT NULL,

    FOREIGN KEY (host_id)
        REFERENCES host (id)
    FOREIGN KEY (guest_id)
        REFERENCES guest (id)
);

INSERT INTO guest VALUES (2, 3, 7), (2, 1, 10), (1, 2, 8)

CREATE TABLE room_reservation (
    id serial PRIMARY KEY,
    guest_id INT NOT NULL,
    room_id INT NOT NULL,
    room_reserved BOOLEAN NOT NULL,
    room_paid BOOLEAN NOT NULL,

    FOREIGN KEY (guest_id)
        REFERENCES guest (id)
    FOREIGN KEY (room_id)
        REFERENCES room (id)
);

INSERT INTO guest VALUES (2, 3, TRUE, TRUE), (2, 1, TRUE, TRUE), (1, 2, TRUE, TRUE)

# Task_1

SELECT name, id FROM guest WHERE MAX(rooms_reserved)

# Task_2

SELECT name, id FROM host WHERE MAX(money_received)

# Task_3

SELECT host_id FROM host_review WHERE MAX(host_rating)

