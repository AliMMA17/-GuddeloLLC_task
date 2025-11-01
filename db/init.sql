CREATE TABLE IF NOT EXISTS users (
  "UserName"  VARCHAR(50) NOT NULL,
  "Birthday"  TIMESTAMP NOT NULL
);

-- sample data
TRUNCATE TABLE users;

INSERT INTO users ("UserName","Birthday") VALUES
  ('Ivan Petrov',        CURRENT_DATE + INTERVAL '0 day'),
  ('Anna Sidorova',      CURRENT_DATE + INTERVAL '1 day'),
  ('Pavel Smirnov',      CURRENT_DATE + INTERVAL '2 days'),
  ('Maria Volkova',      CURRENT_DATE + INTERVAL '3 days'),
  ('Elena Kuznetsova',   CURRENT_DATE + INTERVAL '4 days'),
  ('Dmitry Orlov',       CURRENT_DATE + INTERVAL '5 days'),
  ('Olga Ivanova',       CURRENT_DATE + INTERVAL '6 days'),
  ('Sergey Morozov',     CURRENT_DATE + INTERVAL '7 days'),
  ('Nikolai Fedorov',    CURRENT_DATE + INTERVAL '8 days'),
  ('Svetlana Popova',    CURRENT_DATE + INTERVAL '9 days'),
  ('Andrey Lebedev',     CURRENT_DATE + INTERVAL '10 days'),
  ('Irina Pavlova',      CURRENT_DATE + INTERVAL '11 days'),
  ('Maxim Egorov',       CURRENT_DATE + INTERVAL '12 days'),
  ('Marina Kozlova',     CURRENT_DATE + INTERVAL '13 days');