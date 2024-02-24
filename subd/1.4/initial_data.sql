CREATE TABLE Tour (
    id serial primary key,
    price INT,
    place VARCHAR(255)
);

INSERT INTO Tour (price, place) VALUES (100, 'Paris');
INSERT INTO Tour (price, place) VALUES (150, 'London');
INSERT INTO Tour (price, place) VALUES (200, 'Tokyo');
