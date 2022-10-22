USE jp-db;

DROP TABLE IF EXISTS state;
DROP TABLE IF EXISTS dish;

CREATE TABLE situations
(
  id             INT PRIMARY KEY AUTO_INCREMENT,
  user_id        INT,
  month          INT,
  steps          INT,
  temperature   FLOAT,
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

INSERT INTO situations
    (user_id, month, steps, temperature, latitude, longitude, time_hour, dish_id)
values
    (1, 10, 100, 29, 26.527356, 128.031590, 12, 0),
    (2, 10, 289, 29, 26.527356, 128.031590, 12, 1),
    (3, 10, 300, 29, 26.527356, 128.031590, 12, 2),
    (4, 10, 400, 29, 26.527356, 128.031590, 12, 3),
    (5, 10, 500, 29, 26.527356, 128.031590, 12, 1),
    (6, 10, 600, 29, 26.527356, 128.031590, 12, 1),
    (7, 10, 700, 29, 26.527356, 128.031590, 12, 2),
    (8, 10, 1800, 29, 26.527356, 128.031590, 12, 1),
    (9, 10, 1900, 29, 26.527356, 128.031590, 12, 0),
    (10, 10, 1020, 29, 26.527356, 128.031590, 12, 3);

INSERT INTO dish
    (id, dish)
values
    (0, "カレー"),
    (1, "寿司"),
    (2, "焼き肉"),
    (3, "ハンバーグ"),
    (4, "牛丼"),
    (5, "ハンバーガー"),
    (6, "親子丼"),
    (7, "唐揚げ"),
    (8, "餃子"),
    (9, "ピザ"),
    (10, "オムライス");