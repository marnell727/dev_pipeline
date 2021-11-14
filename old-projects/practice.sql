CREATE TABLE Cars (
    make TEXT NOT NULL,
    model TEXT NOT NULL,
    year INTEGER
);

INSERT INTO Cars (make, model, year)
VALUES('Ford', 'Mustang', '1969');

SELECT * FROM Cars;

ALTER TABLE Cars
RENAME TO Vehicles;