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
  ('Leap Person',    '1996-02-29 00:00:00');