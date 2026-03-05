DROP TABLE IF EXISTS dog;
CREATE TABLE dog (
  id           serial PRIMARY KEY,
  name         varchar(255) NOT NULL,
  breed        varchar(255) NOT NULL,
  color        varchar(255) NOT NULL,
  age           integer
);