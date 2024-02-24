sudo apt install postgresql

sudo -u postgres createdb ptu
sudo -u postgres createuser --superuser `whoami`
sudo -u postgres psql -c "ALTER USER stepan WITH PASSWORD 'stepan'"
psql ptu

sudo apt install postgresql-plpython3

CREATE LANGUAGE plpython3u;
CREATE FUNCTION pymax (a integer, b integer)
  RETURNS integer
AS $$
  if a > b:
    return a
  return b
$$ LANGUAGE plpython3u;
select * from pymax(1, 2);

# psycopg
