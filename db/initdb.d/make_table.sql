USE jp-db;

DROP TABLE IF EXISTS state;
DROP TABLE IF EXISTS dish;

CREATE TABLE state
(
  id             INT PRIMARY KEY,
  month          INT,
  steps          INT,
  temprature   FLOAT,
  latitude     FLOAT,
  longitude    FLOAT,
  time_hour      INT,
  dish_id        INT
);

CREATE TABLE dish
(
    id      INT PRIMARY KEY,
    dish    VARCHAR(100)
);