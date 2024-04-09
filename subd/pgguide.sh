sudo apt install postgresql
sudo apt install postgresql-plpython3

sudo -u postgres createdb ptu
sudo -u postgres createuser --superuser `whoami`
sudo -u postgres psql -c "ALTER USER stepan WITH PASSWORD 'stepan'"
psql ptu
CREATE LANGUAGE plpython3u;
