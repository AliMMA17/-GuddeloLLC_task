CREATE TABLE IF NOT EXISTS users (
  "UserName"  VARCHAR(50) NOT NULL,
  "Birthday"  TIMESTAMP NOT NULL
);

-- sample data
TRUNCATE TABLE users;
INSERT INTO users ("UserName","Birthday") VALUES
  ('Ivan Petrov',    '1997-10-28 00:00:00'),
  ('Anna Sidorova',  '1990-10-29 00:00:00'),
  ('Pavel Smirnov',  '1988-10-30 00:00:00'),
  ('Maria Volkova',  '1995-10-31 00:00:00'),
  ('Leap Person',    '1996-02-29 00:00:00'),
  ('Elena Kuznetsova',   '1992-10-28 13:45:00'),
  ('Dmitry Orlov',       '1984-10-29 09:10:00'),
  ('Olga Ivanova',       '1993-10-30 22:01:00'),
  ('Sergey Morozov',     '1980-10-31 14:25:00'),
  ('New Year One',       '1987-01-01 00:00:00'),
  ('New Year Eve',       '1979-12-31 00:00:00'),
  ('Feb 28 Person',      '1994-02-28 00:00:00'),
  ('Mar 01 Person',      '1995-03-01 00:00:00');